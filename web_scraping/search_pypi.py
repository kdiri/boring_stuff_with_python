"""
.. module:: web_scraping.search_pypi
   :synopsis: search libs on pypi.org and show the results on a different tabs
"""
import webbrowser
from typing import List

import requests
from bs4 import BeautifulSoup

from web_scraping.download_web_page import get_existing_page
from web_scraping.map_it import get_content


def construct_base_query():
    return ["https://google.co.uk"]


def construct_search_query(to_look_for) -> List:
    search_queries = {
        "google": f"https://google.co.uk/search?q={to_look_for}",
        "pypi": f"https://pypi.org/search/?q={to_look_for}",
    }
    return search_queries


def get_input_from_command_line_or_clipboard():
    return get_content()


def make_it_soup(res: requests):
    return BeautifulSoup(res.content, "html.parser")


def parse_results(resp: requests):
    results: list = []
    soup = make_it_soup(resp)
    for g in soup.find_all("div", class_="r"):
        anchors = g.find_all("a")
        if anchors:
            link = anchors[0]["href"]
            title = g.find("h3").text
            item = {"title": title, "link": link}
            results.append(item)
    return results


def orchestrate():
    libraries = get_input_from_command_line_or_clipboard()
    search_queries = construct_search_query(libraries)
    results = get_existing_page(search_queries.get("google", None))
    pages_to_open = parse_results(results)
    for i, page_to_open in enumerate(pages_to_open):
        webbrowser.open(page_to_open.get("link"))
        i += 1
        if i == 3:
            break


if __name__ == "__main__":
    orchestrate()
