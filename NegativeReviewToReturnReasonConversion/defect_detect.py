from google import genai
from google.genai import types

import PIL.Image
import PIL.ImageDraw as ImageDraw
import os
from dotenv import load_dotenv
from pydantic import BaseModel


load_dotenv()


class DefectData(BaseModel):
    description: str
    coordinates: list[int]


client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
image = PIL.Image.open(
    # "/Users/hasnaink/GitHub/HTF/NegativeReviewToReturnReasonConversion/return-policy-on-clothes-v0-5q6z6ex9i9zc1.webp"
    # "/Users/hasnaink/GitHub/HTF/NegativeReviewToReturnReasonConversion/87002900_TM_B.avif"
    # "/Users/hasnaink/GitHub/HTF/NegativeReviewToReturnReasonConversion/istockphoto-1181214322-612x612.jpg"
    # "/Users/hasnaink/GitHub/HTF/NegativeReviewToReturnReasonConversion/moth-holes-720x390.jpg"
    # "/Users/hasnaink/GitHub/HTF/NegativeReviewToReturnReasonConversion/istockphoto-174952369-612x612.jpg"
    "/Users/hasnaink/GitHub/HTF/NegativeReviewToReturnReasonConversion/modal_privacy__fztx4u51s8q6_large.jpg"
)

product_description = "Mobile phone"
product_title = "Mobile Phone"
return_reason = "audio not working"
# return_reason = ""


prompt = (
    f"The image contains the following product \nProduct Title: {product_title} \nProduct Description: {product_description}."
    + (f"\nIt was returned for this reason: {return_reason}" if return_reason else "")
    + f"\nIdentify the defects in the following product image and provide a short one line description of the defect. \nReturn a bounding box for any defects in the product in [ymin, xmin, ymax, xmax] format."
)

response = client.models.generate_content(
    model="gemini-1.5-pro",
    contents=[image, prompt],
    config={
        "response_mime_type": "application/json",
        "response_schema": list[DefectData],
    },
)

# response = client.models.generate_content(
#     model="gemini-2.0-flash", contents=["What is this image?", image]
# )

defects: list[DefectData] = response.parsed
print(defects)

response_text = response.text

# shape = [int(coord) / 1000 for coord in response_text[1:-1].split(",")]
for defect in defects:
    if not defect.coordinates:
        continue
    shape = defect.coordinates
    shape = [shape[1], shape[0], shape[3], shape[2]]

    for i in range(len(shape)):
        if i % 2 == 0:
            shape[i] *= image.width / 1000
        else:
            shape[i] *= image.height / 1000

    img1 = ImageDraw.Draw(image)
    img1.rectangle(shape, outline="red", width=5)

image.show()
