"""
Search where the product sells the best.
"""
from enum import Enum

from google import genai
from google.genai.types import Tool, GenerateContentConfig, GoogleSearch
import os
from typing import Any
from dotenv import load_dotenv
from pydantic import BaseModel, ValidationError
import json
import datetime
from typing import List, Optional

import json
import os
from urllib.parse import urlencode
from urllib.request import urlopen
import urllib.request
import time

load_dotenv()
global result_google_shopping


def price_api_google_shopping(item_name) -> Any:

    API = "https://api.priceapi.com/v2"
    ENDPOINT = "/jobs"
    TOKEN = os.environ["PRICEAPI_TOKEN"]
    search_terms = [
        item_name,
    ]
    job_parameters = {
        "token": TOKEN,
        "source": "google_shopping",
        "country": "us",
        "topic": "product_and_offers",
        "key": "term",
        "values": "\n".join(search_terms),
        # "condition_code": "used",
    }
    response = urlopen(API + ENDPOINT, urlencode(job_parameters).encode())
    result_google_shopping = json.loads(response.read())
    job_id = result_google_shopping["job_id"]
    print("Created job with id:", job_id)
#####################################################################################################################
    ENDPOINT2 = "/jobs/" + job_id
    status = None
    while True:
        time.sleep(5)
        url = API + ENDPOINT2 + "?token=" + TOKEN
        response = urllib.request.urlopen(url).read()
        status = json.loads(response)["status"]
        print("Job status: " + status)

        if status in ["finished", "cancelled"]:
            break

#####################################################################################################################
    ENDPOINT3 = "/jobs/" + job_id + "/download"
    url = API + ENDPOINT3 + "?token=" + TOKEN
    response = urllib.request.urlopen(url)
    result = json.loads(response.read())
    return result


def price_api_ebay(item_name) -> Any:

    API = "https://api.priceapi.com/v2"
    ENDPOINT = "/jobs"
    TOKEN = os.environ["PRICEAPI_TOKEN"]
    search_terms = [
        item_name,
    ]
    job_parameters = {
        "token": TOKEN,
        "source": "ebay",
        "country": "us",
        "topic": "product_and_offers",
        "key": "term",
        "values": "\n".join(search_terms)
    }
    response = urlopen(API + ENDPOINT, urlencode(job_parameters).encode())
    result_google_shopping = json.loads(response.read())
    job_id = result_google_shopping["job_id"]
    print("Created job with id:", job_id)
#####################################################################################################################
    ENDPOINT2 = "/jobs/" + job_id
    status = None
    while True:
        time.sleep(5)
        url = API + ENDPOINT2 + "?token=" + TOKEN
        response = urllib.request.urlopen(url).read()
        status = json.loads(response)["status"]
        print("Job status: " + status)

        if status in ["finished", "cancelled"]:
            break

#####################################################################################################################
    ENDPOINT3 = "/jobs/" + job_id + "/download"
    url = API + ENDPOINT3 + "?token=" + TOKEN
    response = urllib.request.urlopen(url)
    result = json.loads(response.read())
    return result


def price_api_amazon(item_name) -> Any:

    API = "https://api.priceapi.com/v2"
    ENDPOINT = "/jobs"
    TOKEN = os.environ["PRICEAPI_TOKEN"]
    search_terms = [
        item_name,
    ]
    job_parameters = {
        "token": TOKEN,
        "source": "amazon",
        "country": "us",
        "topic": "product_and_offers",
        "key": "term",
        "values": "\n".join(search_terms)
    }
    response = urlopen(API + ENDPOINT, urlencode(job_parameters).encode())
    result_google_shopping = json.loads(response.read())
    job_id = result_google_shopping["job_id"]
    print("Created job with id:", job_id)
#####################################################################################################################
    ENDPOINT2 = "/jobs/" + job_id
    status = None
    while True:
        time.sleep(5)
        url = API + ENDPOINT2 + "?token=" + TOKEN
        response = urllib.request.urlopen(url).read()
        status = json.loads(response)["status"]
        print("Job status: " + status)

        if status in ["finished", "cancelled"]:
            break

#####################################################################################################################
    ENDPOINT3 = "/jobs/" + job_id + "/download"
    url = API + ENDPOINT3 + "?token=" + TOKEN
    response = urllib.request.urlopen(url)
    result = json.loads(response.read())
    return result


def gemini(amazon, ebay, google_shopping, item_name):

    "Generates a better description using the Gemini API."

    class Platform(Enum):
        AMAZON = "amazon"
        EBAY = "ebay"
        GOOGLE_SHOPPING = "google_shopping"
    class DataFormat(BaseModel):
        platform: Platform
        reasoningForListing:str
        price: int
        reasoningForPrice: str


    client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
    full_prompt = (
        f"I want to find the best place to sell {item_name},"
        f"Here are its stats on Amazon: {amazon}."
        f"Here are its stats on Ebay:  {ebay}."
        f"Here are its stats on Google Shopping {google_shopping}."
        f"Tell me the best platform to sell the product on and your reasoning."
        f"In addition, tell me the best and most competetive price to sell it at and your reasoning. "
        f"Try to take into account as many stats as possible."
    )
    print(full_prompt)

    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=full_prompt,
            config={
                "response_mime_type": "application/json",
                "response_schema": DataFormat
            },
        )
        return response.text
    except Exception as e:
        print(f"Error generating content for {item_name}: {e}")
        return None

def main(item_name):
    """
    This will execute all the required files in the order needed
    :return:
    """
    response = gemini(price_api_amazon(item_name), price_api_ebay(item_name),
                      price_api_google_shopping(item_name), item_name)
    print(response)

main("Airpods Pro")
