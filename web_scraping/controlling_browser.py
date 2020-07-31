"""
.. module:: web_scraping.controllling_browser
   :synopsis: control web browser using selenium web driver
"""
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from web_scraping.map_it import get_content


def get_chrome_browser() -> webdriver.Chrome:
    return webdriver.Chrome()


def get_firefox_browser() -> webdriver.Firefox:
    return webdriver.Firefox()


def get_elements_from_site():
    web_site = get_content()
    browser = get_firefox_browser()
    browser.get(web_site)
    try:
        elem = browser.find_element_by_class_name("cover-thumb")
        print(f"Found <{elem.tag_name}> element with that class name!")
    except Exception as exc:
        print(f"Was not able to find an element with that name. {exc}")


def open_given_site(site):
    browser = get_firefox_browser()
    browser.get(site)
    return browser


def sleep_and_close(browser: webdriver.Firefox.get):
    sleep(5)
    browser.close()


def click_to_page():
    web_site = "https://inventwithpython.com/"
    browser = open_given_site(web_site)
    link_elem = browser.find_element_by_link_text("Read Online for Free")
    link_elem.click()
    sleep_and_close(browser)


def fill_send_login(browser, user_name, password):
    user_elem = browser.find_element_by_id("user_name")
    user_elem.send_keys("papa")
    password_elem = browser.find_element_by_id("user_pass")
    password_elem.send_keys("myPass")
    password_elem.submit()
    sleep_and_close(browser)


def fill_and_submit_forms():
    web_site = "https://login.metafilter.com"
    browser = open_given_site(web_site)
    fill_send_login(browser, "papa", "mypass")
    sleep_and_close(browser)


def scroll_page():
    web_site = "https://en.wikipedia.org/wiki/Operation_Cobra"
    browser = open_given_site(web_site)
    html_elem = browser.find_element_by_tag_name("html")
    html_elem.send_keys(Keys.END)
    html_elem.send_keys(Keys.HOME)
    sleep_and_close(browser)


if __name__ == "__main__":
    # get_elements_from_site()
    # click_to_page()
    # fill_and_submit_forms()
    scroll_page()
