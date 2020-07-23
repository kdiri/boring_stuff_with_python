"""
.. module:: web_scraping.map_it
   :synopsis: get place name as an input or take the information of clipboard.
"""

import webbrowser
from pandas.io.clipboard import clipboard_get
from typing import Any


def get_content():
    address = input(
        "Please paste the address or please enter and what it has copied to clipboard will be used: \n"
    )
    if not address:
        address = clipboard_get()
    return address


def open_browser(address: str = Any):
    google_maps = "https://www.google.com/maps/place/"
    webbrowser.open(google_maps + address)


def process():
    address = get_content()
    open_browser(address)


if __name__ == "__main__":
    process()
