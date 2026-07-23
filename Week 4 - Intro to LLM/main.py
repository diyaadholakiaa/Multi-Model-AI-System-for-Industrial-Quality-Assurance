import chainlit as cl
from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def get_gpt_output(user_message):
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {
                "role": "system",
                "content": "You are an assistant that is obsessed with potatoes and will never stop talking about them."
            },
            {
                "role": "user",
                "content": user_message
            }
        ],
        temperature=1,
        max_tokens=256
    )

    return response.choices[0].message.content


@cl.on_message
async def main(message: cl.Message):
    reply = get_gpt_output(message.content)

    await cl.Message(
        content=reply
    ).send()