"""
.. module:: web_scraping.search_pypi
   :synopsis: search libs on pypi.org and show the results on a different tabs
"""
import webbrowser

from web_scraping.download_web_page import get_existing_page
from web_scraping.map_it import get_content
from loguru import logger
from typing import List
from bs4 import BeautifulSoup
import requests


def construct_base_query():
    return ["https://google.co.uk"]


def construct_search_query(to_look_for) -> List:
    search_queries = [
        f"https://google.co.uk/search?q={to_look_for}",
        f"https://pypi.org/search/?q={to_look_for}",
    ]
    return search_queries


def get_input_from_command_line_or_clipboard():
    return get_content()


def make_it_soup(res):
    results = BeautifulSoup(res.text, "lxml")
    for result in results.select(".r a"):
        logger.info(result.next)
    return results


def parse_results(results: requests):
    base = construct_base_query()
    results = make_it_soup(results)

    for next_page in results.select(".fl"):
        res = get_existing_page(base + next_page.get("href"))
        soup = make_it_soup(res)

    return soup


def orchestrate():
    libraries = get_input_from_command_line_or_clipboard()
    search_queries = construct_search_query(libraries)
    for search_query in search_queries:
        i = 0
        logger.info(search_query)
        results = get_existing_page(search_query)
        for result in results:
            logger.info(result)
            webbrowser.open(result)
            i += 1
            if i == 3:
                break


if __name__ == "__main__":
    orchestrate()
