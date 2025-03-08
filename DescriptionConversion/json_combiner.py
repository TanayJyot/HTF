import json
import datetime

try:
    with open("../NegativeReviewToReturnReasonConversion/real_dataset_new.json", "r", encoding="utf-8") as file:
        item_dataset = json.load(file)
except FileNotFoundError:
    print("Error: real_dataset_new.json not found.")
    exit()
except json.JSONDecodeError:
    print("Error: Could not decode real_dataset_new.json. The file may be corrupted.")
    exit()

try:
    with open("../NegativeReviewToReturnReasonConversion/2025-03-07_21-00-44_output.json", "r", encoding="utf-8") as file:
        return_dataset = json.load(file)
except FileNotFoundError:
    print("Error: 2025-03-07_18-58-31_output.json not found.")
    exit()
except json.JSONDecodeError:
    print("Error: Could not decode 2025-03-07_18-58-31_output.json. The file may be corrupted.")
    exit()

# Iterate through both datasets and directly copy name and description
for return_item, item in zip(return_dataset, item_dataset):
    return_item["name"] = item["item name"]
    return_item["description"] = item["item description"]

output_file = f"final_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}_output.json"
try:
    with open(output_file, "w", encoding="utf-8") as out_file:
        json.dump(return_dataset, out_file, indent=4, ensure_ascii=False)
    print(f"Data written to {output_file}")
except IOError as e:
    print(f"Error writing to file {output_file}: {e}")
