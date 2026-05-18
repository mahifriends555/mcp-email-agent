
import json
from pathlib import Path
from datetime import datetime
import time

# Storage path
STORAGE_PATH = Path("app/storage/applications.json")


def _ensure_storage_exists():
    """Create storage file if it doesn't exist or is empty."""
    if not STORAGE_PATH.exists():
        STORAGE_PATH.parent.mkdir(parents=True, exist_ok=True)
        STORAGE_PATH.write_text(json.dumps([], indent=2))
    else:
        # File exists but might be empty - fix it
        content = STORAGE_PATH.read_text().strip()
        if not content:
            STORAGE_PATH.write_text(json.dumps([], indent=2))

def generate_application_id():
    """Generate unique application ID using timestamp."""
    return f"app_{int(time.time())}"


def save_application(parsed_data: dict, generated_email: str, recipient_email: str) -> dict:
    """
    Save application to JSON file.
    
    Args:
        parsed_data: {company, job_title, skills}
        generated_email: email text
        recipient_email: recipient email address
    
    Returns:
        Saved application object with ID, timestamp, status
    """
    _ensure_storage_exists()
    
    # Create application object
    application = {
        "application_id": generate_application_id(),
        "company": parsed_data.get("company", "Unknown"),
        "job_title": parsed_data.get("job_title", "Unknown"),
        "skills": parsed_data.get("skills", []),
        "recipient_email": recipient_email,
        "generated_email": generated_email,
        "status": "pending",
        "timestamp": datetime.now().isoformat()
    }
    
    # Load existing applications
    existing_apps = json.loads(STORAGE_PATH.read_text())
    
    # Add new application
    existing_apps.append(application)
    
    # Save back to file
    STORAGE_PATH.write_text(json.dumps(existing_apps, indent=2))
    
    print(f"\n[✓] Application saved: {application['application_id']}")
    
    return application


def get_all_applications() -> list:
    """Get all saved applications."""
    _ensure_storage_exists()
    return json.loads(STORAGE_PATH.read_text())


def get_application(application_id: str) -> dict:
    """Get specific application by ID."""
    _ensure_storage_exists()
    apps = json.loads(STORAGE_PATH.read_text())
    
    for app in apps:
        if app["application_id"] == application_id:
            return app
    
    return None


def update_application_status(application_id: str, status: str) -> dict:
    """Update application status (e.g., pending -> sent)."""
    _ensure_storage_exists()
    apps = json.loads(STORAGE_PATH.read_text())
    
    for app in apps:
        if app["application_id"] == application_id:
            app["status"] = status
            STORAGE_PATH.write_text(json.dumps(apps, indent=2))
            return app
    
    return None
