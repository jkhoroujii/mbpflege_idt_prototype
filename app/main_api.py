from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings 
from app.routers import auth, staff, patients, medicine, schedules, ai

# creating the app core and set the metadata
app = FastAPI(title=settings.APP_NAME,
              description="Internal Company AI Agent: PROTOTYPE")

# CORS security config; setting rules 
app.add_middleware(
    CORSMiddleware,
    allow_origins=[settings.FRONTEND_URL, "http://localhost:8420"],
    allow_credentials=True,
    allow_methods=["*"], # GET / POST / DELETE / PATCH / OPTIONS
    allow_headers=["*"]) # permits frontend custom headers

# router registration; merge endpoints into the APP / maintain order / expose paths to the public internet
app.include_router(auth.router)
app.include_router(staff.router)
app.include_router(patients.router)
app.include_router(medicine.router)
app.include_router(schedules.route)
app.include_router(ai.router)

# app health checkpoint; group documentation / infrastructure check / define a standard GET checkpoint
@app.get("/health", tags=["meta"])
async def health():
    return {"status": "ok", "app": settings.APP_NAME}