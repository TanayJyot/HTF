"""
Creates return reasons from the negative review dataset for each product
"""

import os
from dotenv import load_dotenv
from google import genai
from pydantic import BaseModel
import json
import datetime
import time

load_dotenv()


class ReturnReason(BaseModel):
    name: str
    description: str
    reviews: list[str]
    returnReason: list[str]


client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

with open("real_dataset.json", "r") as file:
    dataset = json.load(file)


store_data = []
for item in dataset:

    full_prompt = (f" Consider the reviews for the {item} and generate return reasons.")
    response = client.models.generate_content(
        model='gemini-2.0-flash',
        contents=full_prompt,
        config={
            'response_mime_type': 'application/json',
            'response_schema': ReturnReason,
        },
    )

    try:
        item_to_store = json.loads(response.text)
        store_data.append(item_to_store)
    except json.JSONDecodeError:
        print(f"Error decoding responses for {item["item name"]}")

    print(response.text)
    time.sleep(4)

output_file = f"{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}_output.json"

with open(output_file, "w") as out_file:
    json.dump(store_data, out_file, indent=4)
