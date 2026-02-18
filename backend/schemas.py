from pydantic import BaseModel
from typing import Literal

class JobCreate(BaseModel):
    company: str
    role: str
    status: Literal["Applied", "Interview", "Offer", "Rejected"]

class JobResponse(JobCreate):
    id: int

    class Config:
        orm_mode = True

class JobUpdate(BaseModel):
    status: Literal["Applied", "Interview", "Offer", "Rejected"]

