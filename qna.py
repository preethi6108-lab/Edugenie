from google import genai
import os

client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

def answer_question(question):
    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=f"Answer this student's question clearly and simply: {question}"
    )
    return response.text
