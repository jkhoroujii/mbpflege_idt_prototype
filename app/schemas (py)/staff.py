from datetime import datetime
from typing import Optional
from pydantic import BaseModel, EmailStr

# check that data being parsed into the staff SQL model is correctly formatted
class StaffCreate(BaseModel):
    staff_fname : str
    staff_lname : str
    staff_email : EmailStr
    staff_role : str
    send_welcome_email : bool 

class StaffUpdate(BaseModel):
    staff_fname : str
    staff_lname : str
    staff_role : str

class StaffResponse(BaseModel):
    id : int
    staff_fname : str
    staff_lname : str
    staff_email : EmailStr
    staff_role : str
    created_at : datetime 

    model_config = {"from_attributes": True}