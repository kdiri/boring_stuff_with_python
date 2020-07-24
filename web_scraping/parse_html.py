"""
.. module:: web_scraping.parse_html
   :synopsis: parse html files
"""

import bs4
from loguru import logger


def parse():
    res = open("web_scraping/another_example.html")
    no_starch_soup = bs4.BeautifulSoup(res.read(), "html.parser")
    logger.success(no_starch_soup)
    author = no_starch_soup.select("#author")
    logger.info(author)
    logger.info(author[0].attrs)
    logger.info(author[0].getText())


if __name__ == "__main__":
    parse()
