from datetime import date, datetime
from typing import Optional, EmailStr
from pydantic import BaseModel 

### MEDICATION GENERAL ###

class MedicationCreate(BaseModel):
    medicine_id : int
    medicine_name : str 
    medicine_std_dosage : str
    medicine_unit : Optional[str] = "mg"
    medicine_side_effects : Optional[str]
    medicine_stock : int

class MedicationUpdate(BaseModel):
    medicine_name : Optional[str] = None
    medicine_unit : Optional[str] = None
    medicine_side_effects : Optional[str] = None 
    medicine_stock : Optional[str] = None

class MedicationResponse(BaseModel):
    medicine_id : int
    medicine_name : str
    medicine_side_effects : Optional[str] 
    medicine_stock : int 
    medicine_unit : Optional[str] = "mg"
    created_at : datetime 

    model_config = {"from_attributes": True}

### PATIENT MEDICATION ###

class PatientMedicationCreate(BaseModel):
    medicine_id : int
    medicine_dosage : str
    dosage_start_date : date
    dosage_end_date : Optional[date] = None
    medicine_instructions : Optional[str] = None 

class PatientMedicationUpdate(BaseModel):
    dosage_start_date : date 
    dosage_end_date : Optional[date] = None 
    medicine_dosage : str
    medicine_instructions : Optional[str]

class PatientMedicationResponse(BaseModel): 
    medicine_id : int
    patient_id : int 
    prescribed_by : Optional[int]
    medicine_dosage : int 
    dosage_start_date : date 
    dosage_end_date : Optional[date]
    medicine_instructions : Optional[str]
    created_at : datetime 


    model_config = {"from_attributes": True}

### ADMINISTRTION LOG ###

class AdminLogCreate(BaseModel): 
    dosage_given : Optional[str] = None 
    notes : Optional[str] = None 

class AdminLogResponse(BaseModel):
    medicine_log_id : int 
    medicine_id : int
    staff_id : int 
    patient_id : int 
    administered_at : datetime 
    dosage_given : Optional[str] = None 
    medicine_notes : Optional[str] = None 

    model_config = {"from_attributes": True}