from fastapi import FastAPI

from app.models.job_models import JobRequest
from app.services.parser_service import parse_job_description
from app.services.email_service import generate_email

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

    generated_email = generate_email(
        parsed_data
    )

    return {
        "parsed_data": parsed_data,
        "generated_email": generated_email,
        "recipient_email": request.recipient_email
    }