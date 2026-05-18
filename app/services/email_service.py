
from pathlib import Path
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()


def generate_email(job_data: dict):

    prompt_path = Path("app/prompts/email_prompt.txt")

    prompt_template = prompt_path.read_text()

    final_prompt = prompt_template.format(
        company=job_data["company"],
        job_title=job_data["job_title"],
        skills=", ".join(job_data["skills"])
    )

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "user",
                "content": final_prompt
            }
        ],
        temperature=0.7
    )

    content = response.choices[0].message.content

    print("\nRAW RESPONSE:")
    print(repr(content))
    print()

    if not content:
        return "Error: No email generated"

    return content.strip()