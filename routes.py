
import os
from google import genai

client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

def generate_comic(prompt):
    try:
        response = client.models.generate_content(
            model="gemini-3.8-flash",
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

    except Exception:
        return {
            "title": "The Magical Forest",
            "story": "A little rabbit named Coco lived in a magical forest. One day, Coco found a glowing golden key. The key opened a secret door inside a giant tree. Behind the door was a beautiful garden full of friendly animals. Coco and the animals became best friends and lived happily ever after.",
            "scenes": [
                "Coco the rabbit exploring the magical forest.",
                "Coco discovering a glowing golden key.",
                "Coco opening a secret door inside a giant tree.",
                "Coco celebrating with new animal friends."
            ]
        }
        
