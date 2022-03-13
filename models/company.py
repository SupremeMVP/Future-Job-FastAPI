from typing import Optional, List

from pydantic import BaseModel

from models.job_item import JobItem

class Company(BaseModel):
    key: Optional[str] = None
    email: str = 'noreply@supememvp.com'
    name: str
    location: str
    description: Optional[str] = None
    url: Optional[str] = None
    logo: Optional[str] = None
    jobs: Optional[List[str]] = []
    hiring: Optional[bool] = False
    approved: Optional[bool] = False
    fastapi: Optional[bool] = False
    remix: Optional[bool] = False
    deta: Optional[bool] = False
    ip: str = '0.0.0.0'
    consulting: Optional[bool] = False