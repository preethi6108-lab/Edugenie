from google import genai
import os
import json

client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

def generate_quiz(topic):
    prompt = f"""
Create a simple 3-question multiple-choice quiz about {topic}.

Return ONLY valid JSON in this format:
{{
  "topic": "{topic}",
  "quiz": [
    {{
      "question": "question here",
      "options": ["option 1", "option 2", "option 3", "option 4"],
      "answer": "correct option"
    }}
  ]
}}

Make the questions suitable for students.
"""

    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=prompt
    )

    text = response.text.strip()

    if text.startswith("```"):
        text = text.replace("```json", "").replace("```", "").strip()

    return json.loads(text)
