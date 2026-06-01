from groq import Groq
from dotenv import load_dotenv
from search import search_web
import os

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

messages = [
    {
        "role": "system",
        "content": """
You are a helpful AI assistant.

Use internet search results when available.
Answer naturally.
If search data is missing, say you are uncertain.
"""
    }
]

while True:

    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Chat ended.")
        break

    try:

        web_results = search_web(user_input)

        search_text = ""

        for r in web_results:

            title = r.get("title", "")
            body = r.get("body", "")

            search_text += (
                f"Title: {title}\n"
                f"Content: {body}\n\n"
            )

        final_prompt = f"""
User Question:
{user_input}

Internet Results:
{search_text}
"""

        messages.append(
            {
                "role": "user",
                "content": final_prompt
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

        print("\nAI:", ai_reply)

    except Exception as e:

        print("\nError:", e)