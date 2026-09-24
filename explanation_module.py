from google import genai
import os

client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

def explain_concept(topic):
    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=f"""
Explain {topic} to a student in simple language.
Give a short definition, important points, and one example.
"""
    )
    return response.text
