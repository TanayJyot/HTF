from google import genai
from google.genai import types

import PIL.Image
import PIL.ImageDraw as ImageDraw
import os
from dotenv import load_dotenv
from pydantic import BaseModel


load_dotenv()

# person, image of clothing, type of desired fit, demographic, dimensions of sizes for item

person_data = {
    "age": 25,
    "gender": "male",
    "preffered_fit": "normal",
    # "height": 5.8,
    # "weight": 150,
}

dimensions = {
    "S": {"chest": "18 in", "length": "28 in"},
    "M": {"chest": "20 in", "length": "29 in"},
    "L": {"chest": "22 in", "length": "30 in"},
    "XL": {"chest": "24 in", "length": "31 in"},
}


class Recommend_Product(BaseModel):
    # color: str | None
    size: str | None


client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
prod_img = PIL.Image.open(
    "/Users/hasnaink/GitHub/HTF/NegativeReviewToReturnReasonConversion/PXL_20250307_225812811.jpg"
)

user_img = PIL.Image.open(
    "/Users/hasnaink/GitHub/HTF/NegativeReviewToReturnReasonConversion/f3ec47e76b5f2614b1eb8b448cfeef86b9689ade.jpg"
)

product_description = "Polo T-shirt"
product_title = "Polo T-shirt"


prompt = (
    f"The first image contains the following product \nProduct Title: {product_title} \nProduct Description: {product_description}."
    + f"\nIt has the following size chart: {dimensions}"
    + f"\nThe second image contains a photo of a person with the following details: {person_data}" 
    "\nEstimate the size that the person should buy for the product based on the their preferences and the provided size chart for the product."
)

response = client.models.generate_content(
    model="gemini-2.0-flash-thinking-exp",
    contents=[prompt, prod_img, user_img],
    config={
        "response_mime_type": "application/json",
        "response_schema": Recommend_Product,
    },
)

# response = client.models.generate_content(
#     model="gemini-2.0-flash", contents=["What is this image?", image]
# )

recommendation = response.parsed

print(recommendation)
