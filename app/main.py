from fastapi import FastAPI

from app.models.job_models import JobRequest
from app.services.parser_service import parse_job_description

app = FastAPI()


@app.get("/health")
def health_check():

    return {
        "status": "running"
    }


@app.post("/parse-job")
def parse_job(request: JobRequest):

    parsed_data = parse_job_description(
        request.job_description
    )

    return {
        "parsed_data": parsed_data,
        "recipient_email": request.recipient_email
    }
