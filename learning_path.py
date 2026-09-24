from google import genai
import os

client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

def get_learning_path(topic):
    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=f"""
Create a simple learning path for a student who wants to learn {topic}.

Give 5 clear steps, starting from basic concepts and ending with practice.
Use simple language.
"""
    )
    return {
        "topic": topic,
        "steps": response.text
    }
