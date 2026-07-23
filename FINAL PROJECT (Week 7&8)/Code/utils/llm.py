import ollama
from utils.prompts import PROMPT_TEMPLATE

def generate_report(detections):

    prompt = PROMPT_TEMPLATE.format(
        detections=detections
    )

    response = ollama.chat(
        model="llama3.2",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]