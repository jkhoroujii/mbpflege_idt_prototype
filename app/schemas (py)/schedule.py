from pydantic import BaseModel
from datetime import datetime 
from typing import Optional 

class ScheduleCreate(BaseModel):
    staff_id : int 
    patient_id : Optional[list] = None 
    shift_start_time : datetime 
    shift_end_time : datetime 
    shift_type : str 
    shift_notes : Optional[str] = None

class ScheduleUpdate(BaseModel):
    patient_id : Optional[list] = None 
    shift_type : str = None 
    shift_start_time : datetime = None
    shift_end_time : datetime = None 
    shift_notes : Optional[str] = None

class ScheduleResponse(BaseModel):
    staff_id : int 
    patient_id : int 
    shift_type : str 
    shift_start_time : datetime
    shift_end_time : datetime 
    shift_notes : Optional[str]
    created_at : datetime 

    model_config = {"from_attributes": True}