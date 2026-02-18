from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

import models, schemas, crud
from database import engine, get_db

# Create Table
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/jobs", response_model=schemas.JobResponse)
def create_job(job: schemas.JobCreate, db: Session = Depends(get_db)):
    return crud.create_job(db, job)

@app.get("/jobs", response_model=list[schemas.JobResponse])
def read_jobs(db: Session = Depends(get_db)):
    return crud.get_jobs(db)

@app.put("/jobs/{job_id}", response_model=schemas.JobResponse)
def update_job(job_id: int, job: schemas.JobUpdate, db: Session = Depends(get_db)):
    updated_job = crud.update_job_status(db, job_id, job.status)
    if not updated_job:
        raise HTTPException(status_code=404, detail="Job not found")
    return updated_job

@app.delete("/jobs/{job_id}")
def delete_job(job_id: int, db: Session = Depends(get_db)):
    deleted_job = crud.delete_job(db, job_id)
    if not deleted_job:
        raise HTTPException(status_code=404, detail="Job not found")
    return {"message": "Job deleted successfully"}
