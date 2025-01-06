query = "The following is text describing the positions of plants in a garden. Act as an expert in permaculture. Based on the garden layout, how can I optimize plant spacing, companion planting, and sunlight exposure to improve growth and yield? Please provide advice on irrigation efficiency, accessibility for maintenance, suggest specific plants for underplanting, and whether any adjustments should be made to the current arrangement."

import os

from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

def get_advice(plant_position_text, usda_zone):
    api_key = os.environ.get("OPENAI_API_KEY")

    client = OpenAI(
        api_key=api_key,
    )

    prompt = f"{query} I am located in zone {usda_zone}. {plant_position_text}"

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content.strip()
