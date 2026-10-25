import os
import json
from PIL import Image
from google import genai

# ---------------------------------------------------
# Gemini Client
# ---------------------------------------------------

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError("GEMINI_API_KEY not found in Hugging Face Secrets.")

client = genai.Client(api_key=API_KEY)

# ---------------------------------------------------
# Analyze Meal
# ---------------------------------------------------

def analyze_meal(image):

    prompt = """
You are a food recognition AI.

Look ONLY at the uploaded meal image.

Identify every visible food item.

Return ONLY valid JSON.

Example:

{
  "foods":[
    "Rice",
    "Chicken",
    "Carrot",
    "Broccoli"
  ],
  "meal_description":"Grilled chicken served with rice and vegetables."
}

Rules:

- JSON only
- No markdown
- No explanations
- No nutrition values
- Food names should be simple (Rice, Chicken, Fish, Bread, Egg...)
"""

    try:

        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=[
                prompt,
                image
            ]
        )

        text = response.text.strip()

        # Remove markdown if Gemini returns it
        if text.startswith("```"):
            text = text.replace("```json", "")
            text = text.replace("```", "")
            text = text.strip()

        data = json.loads(text)

        return data

    except Exception as e:

        print(e)

        return {
            "foods": [],
            "meal_description": "",
            "error": str(e)
        }
