
from pathlib import Path

# ======================================================
# MCP Email Agent - Project Structure Generator
# ======================================================
# Run this file once to create the complete folder structure.
# Command:
# python create_structure.py
# ======================================================

# Root project path
ROOT_DIR = Path(".")

# Folders to create
folders = [
    "app",
    "app/config",
    "app/routers",
    "app/services",
    "app/models",
    "app/prompts",
    "app/utils",
    "app/storage",
    "tests",
]

# Files to create
files = [
    "app/main.py",
    "app/config/settings.py",
    "app/routers/application_router.py",
    "app/services/parser_service.py",
    "app/services/email_service.py",
    "app/services/drive_service.py",
    "app/services/sheets_service.py",
    "app/models/job_models.py",
    "app/prompts/extraction_prompt.txt",
    "app/prompts/email_prompt.txt",
    "app/utils/helpers.py",
    "app/storage/applications.json",
    ".env",
    ".gitignore",
    "README.md",
]


# ======================================================
# Create folders
# ======================================================
for folder in folders:
    folder_path = ROOT_DIR / folder
    folder_path.mkdir(parents=True, exist_ok=True)
    print(f"[+] Folder created: {folder}")


# ======================================================
# Create files
# ======================================================
for file in files:
    file_path = ROOT_DIR / file

    # Create parent directories if missing
    file_path.parent.mkdir(parents=True, exist_ok=True)

    # Create file only if it doesn't exist
    if not file_path.exists():
        file_path.touch()
        print(f"[+] File created: {file}")
    else:
        print(f"[=] Already exists: {file}")


print("\nProject structure setup completed successfully!")
