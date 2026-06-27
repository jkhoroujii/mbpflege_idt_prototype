from pydantic import BaseModel

class AskAI(BaseModel):
    query : str

class ResponseAI(BaseModel):
    response : str 

class SummarizeNotesAI(BaseModel):
    patient_id : int 
    summary : str 