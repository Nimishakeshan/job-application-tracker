from sqlalchemy.orm import Session
from models import Job
from schemas import JobCreate

def create_job(db: Session, job: JobCreate):
    new_job = Job(
        company=job.company,
        role=job.role,
        status=job.status
    )
    db.add(new_job)
    db.commit()
    db.refresh(new_job)
    return new_job

def get_jobs(db: Session):
    return db.query(Job).all()

def update_job_status(db: Session, job_id: int, status: str):
    job = db.query(Job).filter(Job.id == job_id).first()
    if not job:
        return None

    job.status = status
    db.commit()
    db.refresh(job)
    return job


def delete_job(db: Session, job_id: int):
    job = db.query(Job).filter(Job.id == job_id).first()
    if not job:
        return None

    db.delete(job)
    db.commit()
    return job

