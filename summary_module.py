from google import genai
import os

client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

def summarize_text(text):
    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=f"""
Summarize the following educational text in simple language.
Keep the important points and make it concise.

Text:
{text}
"""
    )
    return response.text
