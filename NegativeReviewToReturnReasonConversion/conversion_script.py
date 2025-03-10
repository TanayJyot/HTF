import os
from dotenv import load_dotenv
from google import genai
from pydantic import BaseModel, ValidationError
import json
import datetime
from typing import List, Optional

load_dotenv()


class ReturnReason(BaseModel):
    name: str
    description: str
    reviews: List[str]
    returnReason: List[str]


client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# Load the dataset
try:
    with open("real_dataset_new.json", "r", encoding="utf-8") as file:
        dataset = json.load(file)
except FileNotFoundError:
    print("Error: real_dataset_new.json not found.")
    exit()
except json.JSONDecodeError:
    print("Error: Could not decode real_dataset_new.json.  The file may be corrupted.")
    exit()


def generate_return_reasons(item):
    """Generates return reasons for a given item using the Gemini API."""
    item_name = item.get("item name", "Unknown Item")  # Provide a default
    full_prompt = (
        f"Consider the following reviews: {item.get("reviews", "No Reviews")}"
        f"  for the {item_name} with {item.get("item description", "no description")} and generate return reasons."


    )  # Ensure item name is included

    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=full_prompt,
            config={
                "response_mime_type": "application/json",
                "response_schema": ReturnReason,
            },
        )
        return response.text

    except Exception as e:
        print(f"Error generating content for {item_name}: {e}")
        return None


store_data = []
for item in dataset:
    response_text = generate_return_reasons(item)

    if response_text:
        try:
            item_to_store = json.loads(response_text)
            store_data.append(item_to_store)
        except json.JSONDecodeError:
            print(f"Error decoding JSON for {item.get('item name', 'Unknown Item')}")
        except ValidationError as e:
            print(f"Validation Error for {item.get('item name', 'Unknown Item')}: {e}")

# Output the data to a JSON file
output_file = f"{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}_output.json"
try:
    with open(output_file, "w") as out_file:
        json.dump(store_data, out_file, indent=4)
    print(f"Data written to {output_file}")
except IOError as e:
    print(f"Error writing to file {output_file}: {e}")
