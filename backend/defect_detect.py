from google import genai
from google.genai import types

import PIL.Image
from PIL.Image import Image
import PIL.ImageDraw as ImageDraw
import os
from dotenv import load_dotenv
from pydantic import BaseModel


load_dotenv()


class DefectData(BaseModel):
    description: str
    coordinates: list[int]


client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def detect_defects(
    product_description, product_title, return_reason, image: Image
) -> tuple[Image, list[DefectData]]:
    prompt = (
        f"The image contains the following product \nProduct Title: {product_title} \nProduct Description: {product_description}."
        + (
            f"\nIt was returned for this reason: {return_reason}"
            if return_reason
            else ""
        )
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

    return image, defects


if __name__ == "__main__":
    image = PIL.Image.open(
        # "/Users/hasnaink/GitHub/HTF/NegativeReviewToReturnReasonConversion/images/defective_teal_shorts.webp"
        "/Users/hasnaink/GitHub/HTF/NegativeReviewToReturnReasonConversion/images/cracked_phone.jpg"
    )
    image.show()

    product_description = "Mobile phone"
    product_title = "Mobile Phone"
    return_reason = "audio not working"
    # return_reason = ""

    return_img = detect_defects(product_description, product_title, return_reason, image)
    image.show()
