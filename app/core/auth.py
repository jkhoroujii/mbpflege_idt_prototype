import bcrypt
from database.db import update, select
from datetime import datetime, timedelta, timezone
from email_wrapper import send_reset_email
import secrets
from db import update

def hash_password(staff_password : str):
    password_bytes = staff_password.encode('utf-8')
    pass_salt = bcrypt.gensalt()
    hashed_bytes = bcrypt.hashpw(password_bytes, pass_salt)
    return hashed_bytes.decode('utf-8')

def check_password(staff_password : str, hashed_password : str):
    password_bytes = bcrypt.hashpw(staff_password.encode('utf-8'), bcrypt.gensalt())
    hashed_bytes = hashed_password.encode('utf-8')
    return bcrypt.checkpw(password_bytes, hashed_bytes)

def create_staff_account(staff_fname : str, staff_lname : str, staff_email : str, staff_password : str):
    hashed_password = hash_password(staff_password)
    # Insert into database (staff table) with hashed password
    return schema.sql.update(
        "INSERT INTO staff (staff_fname, staff_lname, staff_email, staff_password) VALUES (%s, %s, %s, %s)",
        (staff_fname, staff_lname, staff_email, hashed_password)
    )
    if hashed_password is None: 
        raise ValueError("Password error: Failed to hash password.")

def verify_staff_login(staff_email : str, staff_password : str) -> dict:
    rows = select("SELECT staff_password FROM staff WHERE staff_email = %s", (staff_email,))
    if not rows:
        return None
    user = rows[0]
    if check_password(staff_password, user['hashed_password']):
        return dict(user)
    return None


### PASSWORD RESETS ###
def reset_password_initiate(staff_email : str):
    user_exists = select("select staff_email from staff where staff_email = %s", (staff_email,))
    if user_exists:
        raw_token = secrets.token_hex(64)
        token_hash = hash_password(raw_token)
        expiration_time = datetime.now() + timedelta(minutes=15)
        update(staff_email, token_hash, expiration_time)
    send_reset_email(staff_email, raw_token)

def reset_password_finalise(staff_email : str, raw_token : str, new_password : str):
    row = select(staff_email)
    if row is None:
        return False
    stored_hash = row[0]["reset_token_hash"]
    expiration_time = row[0]["reset_token_expires"]
    if stored_hash is None: 
        return False
    if expiration_time is None:
        return False 
    
    submitted_token = hash_password(raw_token)
    tokens_match = secrets.compare_digest

    time_now = datetime.now(timezone.aest)
    if time_now > expiration_time:
        return False # token expired
    if not tokens_match:
        return False # wrong token