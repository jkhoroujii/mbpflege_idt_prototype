from datetime import date, datetime 
from typing import Optional, EmailStr
from pydantic import BaseModel

class PatientCreate(BaseModel):
    staff_fname : str
    staff_lname : str
    patient_dob : Optional[date]
    patient_gender : str
    patient_phone : Optional[str]
    patient_email : EmailStr 
    patient_notes : Optional[str]

class PatientUpdate(BaseModel):
    staff_fname : str
    staff_lname : str
    patient_dob : Optional[date]
    patient_gender : str
    patient_phone : Optional[str]
    patient_email : EmailStr 
    patient_notes : Optional[str]


class PatientResponse(BaseModel):
    id : int
    patient_fname : str
    patient_lname : str
    patient_dob : Optional[date] = None 
    patient_gender : str
    patient_phone : Optional[str]
    patient_email : EmailStr
    patient_notes : Optional[str]
    created_at : datetime
    updated_at : datetime 

    model_config = {"from_attributes": True}