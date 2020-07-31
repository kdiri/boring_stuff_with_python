"""
.. module:: parsing_csv_and_json_files.manipulate_json_file
   :synopsis: Read, write json files
"""
import json
from web_scraping.download_web_page import get_existing_page
from loguru import logger
import requests
from datetime import datetime

API_KEY = "***"


def get_input():
    location = input("Enter city name(Ex: Paris): ")
    return "".join(location)


def construct_url(location: str) -> requests.get:
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={API_KEY}"
    return get_existing_page(url)


def convert_fahr_to_celcius(temparature: int = 0):
    return float(temparature) - 273.15


def parse(res: dict):
    logger.success(f"The weather is {res['weather'][0]['main']}")
    "°C"
    mean_ = convert_fahr_to_celcius(res["main"]["temp"])
    min_ = convert_fahr_to_celcius(res["main"]["temp_min"])
    max_ = convert_fahr_to_celcius(res["main"]["temp_max"])
    sun_rise = datetime.fromtimestamp(res["sys"]["sunrise"]).strftime("%A, %B %d, %Y %I:%M:%S")
    sun_set = datetime.fromtimestamp(res["sys"]["sunset"]).strftime("%A, %B %d, %Y %I:%M:%S")
    logger.success(f"The temparature is {mean_}")
    logger.success(f"The min temparature is {min_}")
    logger.success(f"The max temparature is {max_}")
    logger.success(f"The sun rise time is {sun_rise} AM")
    logger.success(f"The sun set time is {sun_set} PM")


def process():
    location = get_input()
    response = construct_url(location)
    res = json.loads(response.text)
    logger.info(res)
    parse(res)



if __name__ == "__main__":
    process()
