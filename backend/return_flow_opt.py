import requests
import json
import os
from dotenv import load_dotenv
from google import genai
from pydantic import BaseModel

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


class Recommend_Service(BaseModel):
    # color: str | None
    service_code: str | None
    service_name: str | None
    reasoning: str | None


def get_return_data_options(to_addr: dict[str, str], from_addr: dict[str, str], product_details: dict[str, str], date: str):
    req_url = "https://secureship.ca/ship/api/v1/carriers/rates"
    headers = {
        "Content-Type": "application/json",
        "X-API-KEY": f"{os.getenv('SECURESHIP_API_KEY')}"
        }

    res = requests.post(req_url, headers=headers, json={
        "fromAddress": from_addr,
        "toAddress": to_addr,
        "packages": [product_details],
        "shipDateTime": date
    })

    # print(res.text)

    return res.text

def predict_service(userAddress: dict[str, str], inventoryAddress: dict[str, str], product_details: dict[str, str], shippingDate: str):
    return_data = get_return_data_options(
        userAddress, inventoryAddress, product_details, shippingDate
    )

    prompt = f"A product needs to be returned. Following are the available return options for the product: {return_data}. Analyse the return options provide the most cost effective and time efficient option overall."

    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=[prompt],
        config={
            "response_mime_type": "application/json",
            "response_schema": Recommend_Service,
        },
    )

    return response.parsed


if __name__ == "__main__":

    userAddress = {
            "addr1": "1500 Bank St.",
            "countryCode": "CA",
            "postalCode": "K1K1K1",
            "city": "Ottawa",
        }
    inventoryAddr = {
            "addr1": "1500 Bank St.",
            "countryCode": "CA",
            "postalCode": "K1K1K1",
            "city": "Ottawa"
        }
    product_details = {
                "packageType": "MyPackage",
                "userDefinedPackageType": "Refrigerator",
                "weight": 23,
                "weightUnits": "Lbs",
                "length": 19,
                "width": 230,
                "height": 430,
                "dimUnits": "Inches",
                "description": "Gift for darling"
            }

    shippingDate = "2019-08-24T14:15:22Z"

    print(predict_service(userAddress, inventoryAddr, product_details, shippingDate))