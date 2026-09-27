import os
from google import genai

client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

def generate_comic(prompt):
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=f"""
        Create a simple 4-scene comic story based on this idea:

        {prompt}

        Give:
        1. A comic title
        2. A short story
        3. Four scenes
        """
    )

    return {
        "title": "AI Comic Story",
        "story": response.text,
        "scenes": []
    }
