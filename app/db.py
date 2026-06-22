from datetime import datetime
import os
from dotenv import load_dotenv
import psycopg2
from psycopg2.extras import RealDictCursor
from psycopg2 import sql

load_dotenv()
api_key = os.getenv("API_KEY")

def get_connection(): # create and return conection to DB only
    """open a connection for the postgresql databaseand return the connection
    read everything from .env
    realdictcursor returns all data as a dictionary (per row)
    """
    try:
        connection = psycopg2.connect(
        host=os.getenv("DB_HOST"),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        port=os.getenv("DB_PORT"),
        cursor_factory=RealDictCursor
    )
        return connection
    
    except Exception as e:
        print(f"Error connecting to the database: {e}")
        return None

def select(sql_string: str, params: tuple = ()) -> list[dict]: # return list of dicts (rows)
    """run a search query and return all rows matching that query as a list of dicts
    """
    db_connection = get_connection()
    try:
        with db_connection.cursor() as cursor:
            cursor.execute(sql_string, params)
            return cursor.fetchall()
    except Exception as e:
        print(f"Error executing query: {e}")
        return []
    finally:
        db_connection.close()

def update(sql_string: str, params: tuple = ()) -> bool: # return True if successful 
    """ run insert/delete/update query on the database
    return true if successful 
    commit changes to postgre db, rollback partial changes"""
    db_connection = get_connection()
    try: 
        with db_connection.cursor() as cursor:
            cursor.execute(sql_string, params)
        db_connection.commit()
        print("Database update successful")
        return True 
    except Exception as e:
        print(f"Error executing insert: {e}")
        db_connection.rollback()
        return False
    finally:
        db_connection.close()

def log_audit(staff_id: int, action: str, time: datetime, ip_address: str) -> None:
    """ write a log entry to the audit_log table whenever the DB is accessed for login (successful or not),
    who did what, when, and where from (IP)"""

    successful_update = update(
        """
        INSERT INTO audit_log (staff_id, action, time, ip_address) 
        VALUES (%s, %s, %s, %s)
        """,
        (staff_id, action, time, ip_address)
    )
    if not successful_update:
        print(f"CRITICAL: Access for staff_id: {staff_id} failed")