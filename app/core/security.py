from datetime import datetime, timedelta, timezone
from typing import Optional 
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from passlib.context import CryptContext
import asyncpg

from app.core.config import Settings
from app.db import get_db 
from app.database.models import Staff

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

### PASSWORDS ###

def hash_password(original_password): 
    return pwd_context.hash(original_password)

def verify_password(original_password, hashed_password): 
    return pwd_context.verify(original_password, hashed_password)

### JWT ###

def create_access_token(data, expires_at): 
    data_to_encode = data.copy()
    token_expiration = datetime.now(timezone.utc) + (expires_at or timedelta(minutes=Settings.ACCESS_TOKEN_EXPIRE_MINS))
    data_to_encode.update({"exp": token_expiration})
    return jwt.encode(data_to_encode, Settings.SECRET_KEY)

def decode_token(token): 
    try:
        return jwt.decode(token, Settings.SECRET_KEY)
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Login kann nicht genehmigen"
            headers={"WWW-Authenticate": "Bearer"}
        )

### CURRENT USER DEPENDENCY ###

async def get_current_staff(token : str, conn : asyncpg.Connection = Depends(get_db)) -> Staff:
    staff_id : Optional[str] 
    if staff_id is None: 
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalide Merkmal")
    
    row = await conn.fetchrow(
        "SELECT staff_id, staff_fname, staff_lname, staff_email, staff_role WHERE staff_id = $1", 
        int(staff_id)
    )
    if row is None: 
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Nutzer nicht gefunden")
    else:
        return dict(row)
    

def require_role(*roles : str): # checks to see if the access is allowed
    async def _check(current : dict = Depends(get_current_staff)):
        if current["staff_role"] not in roles: 
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Begrenzt Erlaubnis")
        return current 
    return _check