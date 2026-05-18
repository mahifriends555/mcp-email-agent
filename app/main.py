from fastapi import FastAPI
from app.models.job_models import JobRequest

# Create FastAPI application
app = FastAPI()


# Health check endpoint
@app.get("/health")
def health_check():
    return {
        "status": "running"
    }


# Parse job endpoint
@app.post("/parse-job")
def parse_job(request: JobRequest):

    return {
        "message": "Job received successfully",
        "job_description": request.job_description,
        "recipient_email": request.recipient_email
    }
