from google import genai
from google.genai import types

import PIL.Image
import PIL.ImageDraw as ImageDraw
import os
from dotenv import load_dotenv
from pydantic import BaseModel
import turtle


load_dotenv()

# person, image of clothing, type of desired fit, demographic, dimensions of sizes for item

class Recommend_Product(BaseModel):
    # color: str | None
    size: str | None


client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def get_optimum_sizes(product_title, product_description, dimensions, person_data, product_image, user_image=None) -> Recommend_Product:
    
    prompt = (
        f"The first image contains the following product \nProduct Title: {product_title} \nProduct Description: {product_description}."
        + f"\nIt has the following size chart: {dimensions}"
        + f"\nThe second image contains a photo of a person with the following details: {person_data}"
        "\nEstimate the size that the person should buy for the product based on the their preferences and the provided size chart for the product."
    )

    contents = [prompt]
    if product_image:
        contents.append(product_image)
    if user_image:
        contents.append(user_image)

    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=[prompt, product_image, user_image],
        config={
            "response_mime_type": "application/json",
            "response_schema": Recommend_Product,
        },
    )

    # response = client.models.generate_content(
    #     model="gemini-2.0-flash", contents=["What is this image?", image]
    # )

    recommendation = response.parsed
    return recommendation


if __name__ == "__main__":
    prod_img = PIL.Image.open(
    "/Users/hasnaink/GitHub/HTF/NegativeReviewToReturnReasonConversion/images/person.jpg"
    )

    user_img = PIL.Image.open(
        "/Users/hasnaink/GitHub/HTF/NegativeReviewToReturnReasonConversion/images/test_shirt.jpg"
    )

    product_description = "Polo T-shirt"
    product_title = "Polo T-shirt"

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

    recommendation = get_optimum_sizes(
        product_title,
        product_description,
        dimensions,
        person_data,
        prod_img,
        user_img,
    )

    turtle.write("hello")
    

    print(recommendation)

# print(recommendation)
