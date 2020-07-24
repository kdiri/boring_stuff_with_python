"""
.. module:: web_scraping.download_web_page
   :synopsis: download web pages using requests module
"""
import sys
from typing import Any

import requests
from loguru import logger

logger.add(sys.stdout, colorize=True, format="<green>{time}</green> <level>{message}</level>")


def get_existing_page(address: str = "") -> Any:
    if not address:
        page = requests.get("https://automatetheboringstuff.com/files/rj.txt")
    else:
        page = requests.get(address)

    page.raise_for_status()
    return page


@logger.catch
def get_404():
    page = requests.get("https://inventwithpython.com/page_that_does_not_exist")
    page.raise_for_status()


def get_safe_404():
    try:
        page = requests.get("https://inventwithpython.com/page_that_does_not_exist")
        page.raise_for_status()
    except Exception as e:
        logger.error(f"Error occurred: {e}")


def save_page():
    iter_cont = 100_000
    page = get_existing_page()
    page.raise_for_status()
    play_file = open("web_scraping/RomeoAndJuliet.txt", "wb")
    for chunk in page.iter_content(iter_cont):
        play_file.write(chunk)
    play_file.close()


if __name__ == "__main__":
    save_page()
    get_safe_404()
    get_404()
