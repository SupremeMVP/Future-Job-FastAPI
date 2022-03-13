from typing import Optional

from fastapi import FastAPI, HTTPException
from fastapi.encoders import jsonable_encoder

from deta import Deta  # Import Deta

from config import settings

from models.job_item import JobItem
from models.company import Company

deta = Deta(settings.deta_key) # ENV this key a duh.
job_db = deta.Base(settings.job_base)
co_db = deta.Base(settings.company_base)

app = FastAPI()

@app.get("/")
def read_root():
    return {
        "Hello": settings.app_name
    }


# Create Company listing
@app.put("/company/")
async def create_company(company: Company):
    json_compatible_company_data = jsonable_encoder(company)
    company = co_db.put(json_compatible_company_data)
    if company is None:
        raise HTTPException(status_code=404, detail="Company not found")

    del company['email']
    del company['ip']

    return company


# Update Company by key
@app.post("/company/")
async def update_company(company: Company):
    json_compatible_company_data = jsonable_encoder(company)
    if json_compatible_company_data['key'] is None:
        raise HTTPException(status_code=404, detail="Company key required")

    company = co_db.put(json_compatible_company_data, json_compatible_company_data['key'])

    if company is None:
        raise HTTPException(status_code=404, detail="Company not found")

    del company['email']
    del company['ip']

    return company


# Get Company by key
@app.get("/company/{key}")
async def read_company(key: Optional[str] = None):
    company = co_db.get(key)
    if company is None:
        raise HTTPException(status_code=404, detail="Company not found")
    
    del company['email']
    del company['ip']

    return company


# Fetch All Companies w/ limits
@app.get("/companies/")
async def fetch_companies(limit: Optional[int] = None, last: Optional[str] = None):
    if last:
        companies = co_db.fetch({"approved": True}, limit=limit, last=last)
    elif limit:
        companies = co_db.fetch({"approved": True}, limit=limit)
    else:
        companies = co_db.fetch({"approved": True})

    if companies is None:
        raise HTTPException(status_code=404, detail="Companies not found")

    json_compatible_companies_data = jsonable_encoder(companies)

    # Clean up Data
    for company in json_compatible_companies_data["_items"]:
        if company['email']:
            del company['email']
            del company['ip']

    return json_compatible_companies_data


# Create Job listing
@app.put("/job/")
async def create_job(job: JobItem):
    json_compatible_job_data = jsonable_encoder(job)
    job = job_db.put(json_compatible_job_data)
    if job is None:
        raise HTTPException(status_code=404, detail="Job not found")

    return job


# Update job by key
@app.put("/job/")
async def update_job(Job: JobItem):
    if Job.key is None:
        raise HTTPException(status_code=404, detail="Job key required")

    Job = co_db.put(Job, Job.key)

    if Job is None:
        raise HTTPException(status_code=404, detail="Job not found")

    return Job



# Get Job listing by key
@app.get("/job/{key}")
async def read_job(key: Optional[str] = None):
    job = job_db.get(key)
    if job is None:
        raise HTTPException(status_code=404, detail="Job not found")

    return job


# Fetch All Jobs w/ limits
@app.get("/jobs/")
async def fetch_jobs(limit: int = 1, last: Optional[str] = None):
    if last:
        jobs = job_db.fetch(limit=limit, last=last)
    else:
        jobs = job_db.fetch(limit=limit)

    if jobs is None:
        raise HTTPException(status_code=404, detail="Jobs not found")

    return jobs
