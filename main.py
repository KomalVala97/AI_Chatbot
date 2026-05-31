from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

messages = [
    {
        "role": "system",
        "content": "You are a helpful assistant."
    }
]

while True:

    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Chat ended.")
        break

    messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )

    response = client.chat.completions.create(
        messages=messages,
        model="llama-3.1-8b-instant"
    )

    ai_reply = response.choices[0].message.content

    messages.append(
        {
            "role": "assistant",
            "content": ai_reply
        }
    )

    print("AI:", ai_reply)