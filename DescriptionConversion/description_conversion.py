"""
This file converts descriptions
"""
import os
from dotenv import load_dotenv
from google import genai
from pydantic import BaseModel, ValidationError
import json
import datetime
from typing import List, Optional

load_dotenv()

class BetterDescription(BaseModel):
    name: str
    old_description: str
    returnReason: List[str]
    new_description: str

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

try:
    with open("final_2025-03-07_21-24-25_output.json", "r", encoding="utf-8") as file:
        dataset = json.load(file)
except FileNotFoundError:
    print("Error: real_dataset_new.json not found.")
    exit()
except json.JSONDecodeError:
    print("Error: Could not decode real_dataset_new.json.  The file may be corrupted.")
    exit()

def generate_better_description(item):
    "Generates a better description using the Gemini API."
    item_name = item.get("name")
    item_description = item.get("description")
    item_return_reasons = item.get("returnReason")

    full_prompt = (
        f"For the {item_name} with the following {item_description}"
        f"and the following return reasons: {item_return_reasons}, "
        f"Create better descriptions that represent the item more accurately."
    )

    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=full_prompt,
            config={
                "response_mime_type": "application/json",
                "response_schema": BetterDescription
            },
        )
        return response.text
    except Exception as e:
        print(f"Error generating content for {item_name}: {e}")
        return None

store_data = []
for item in dataset:
    response_text = generate_better_description(item)
    if response_text:
        try:
            item_to_store = json.loads(response_text)
            store_data.append(item_to_store)
        except json.JSONDecodeError:
            print(f"Error decoding JSON for {item.get('item name', 'Unknown Item')}")
        except ValidationError as e:
            print(f"Validation Error for {item.get('item name', 'Unknown Item')}: {e}")

# Output the data to a JSON file
output_file = f"better_descriptions_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}_output.json"
try:
    with open(output_file, "w") as out_file:
        json.dump(store_data, out_file, indent=4)
    print(f"Data written to {output_file}")
except IOError as e:
    print(f"Error writing to file {output_file}: {e}")
