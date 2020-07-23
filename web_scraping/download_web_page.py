"""
.. module:: web_scraping.download_web_page
   :synopsis: download web pages using requests module
"""
import requests
from loguru import logger


def get_existing_page():
    page = requests.get("https://automatetheboringstuff.com/files/rj.txt")
    assert page.status_code == requests.codes.ok
    logger.info(page.text[:250])
    return page


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
    page = get_existing_page()
    page.raise_for_status()
    play_file = open("web_scraping/RomeoAndJuliet.txt", "wb")
    for chunk in page.iter_content(100_000):
        play_file.write(chunk)
    play_file.close()


if __name__ == "__main__":
    save_page()
    get_safe_404()
