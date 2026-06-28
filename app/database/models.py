from dataclasses import dataclass, field
from datetime import date, datetime 
from typing import Optional
from decimal import Decimal

### STAFF ###

class Staff: 
    staff_id : int 
    staff_fname : str
    staff_lname : str
    staff_email : str
    staff_hashed_password : str
    staff_role : str 
    staff_created_at : datetime 

class StaffCredentials:
    staff_id : int 
    hashed_password : str
    created_at : datetime 
    updated_at : datetime 

class PasswordResetToken:
    staff_id : int 
    token : str 
    created_at : datetime
    expires_at : datetime  

### SYSTEM LOGS ###

class LoginLog: 
    staff_id : int 
    staff_email : str 
    staff_ip_address : str
    created_at : datetime 

class DatabaseAccessLog: 
    staff_id : int 
    staff_ip_address :str
    action : str
    created_at : datetime  

class PasswordChangeLog:
    staff_id : int 
    staff_ip_address : str 
    created_at : datetime 

### PATIENT LOGS ###

class Patient:
    patient_id : int 
    patient_fname : str
    patient_lname : str 
    patient_dob : date
    patient_gender : str
    patient_phone : Optional[str] = None 
    patient_notes : Optional[str] = None 
    created_at : datetime 

class Medicine: 
    medicine_id : int 
    medicine_name : str 
    medicine_stock : int 
    medicine_frequency : Decimal 
    medicine_side_effects : Optional[str] = None 
    created_at : datetime 

class PatientMedication: 
    pass

class PatientMedsAdministrationLog: 
    pass

### OTHER ###

class Schedule:
    pass 

