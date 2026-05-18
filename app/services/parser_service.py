
import json
from pathlib import Path

from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()


def parse_job_description(job_description: str):

    prompt_path = Path("app/prompts/extraction_prompt.txt")
    prompt_template = prompt_path.read_text()
    final_prompt = prompt_template.format(
        job_description=job_description
    )

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "user",
                "content": final_prompt
            }
        ],
        temperature=0
    )

    content = response.choices[0].message.content
    return json.loads(content)
