"""
.. module:: parsing_csv_and_json_files.manipulate_json_file
   :synopsis: Read, write json files
"""
import json
from web_scraping.download_web_page import get_existing_page
from loguru import logger
import requests

API_KEY = "***"


def get_input():
    location = input("Enter city name(Ex: Paris): ")
    return "".join(location)


def construct_url(location: str) -> requests.get:
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={API_KEY}"
    return get_existing_page(url)


def process():
    location = get_input()
    response = construct_url(location)
    res = json.loads(response.text)
    logger.info(res)


if __name__ == "__main__":
    process()
