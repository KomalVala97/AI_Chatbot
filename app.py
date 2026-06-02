import gradio as gr
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

def chatbot(message, history):

    messages.append(
        {
            "role": "user",
            "content": message
        }
    )

    response = client.chat.completions.create(
        messages=messages,
        model="llama-3.3-70b-versatile"
    )

    ai_reply = (
        response
        .choices[0]
        .message
        .content
    )

    messages.append(
        {
            "role": "assistant",
            "content": ai_reply
        }
    )

    return ai_reply


app = gr.ChatInterface(
    fn=chatbot
)

app.launch(
    share=True
)