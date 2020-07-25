from selenium import webdriver

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


def click_to_page():
    web_site = "https://inventwithpython.com/"
    browser = open_given_site(web_site)
    link_elem = browser.find_element_by_link_text("Read Online for Free")
    link_elem.click()


def fill_and_submit_forms():
    web_site = "https://login.metafilter.com"
    browser = open_given_site(web_site)
    user_elem = browser.find_element_by_id("user_name")
    user_elem.send_keys("papa")
    password_elem = browser.find_element_by_id("user_pass")
    password_elem.send_keys("myPass")
    password_elem.submit()


if __name__ == "__main__":
    # get_elements_from_site()
    # click_to_page()
    fill_and_submit_forms()
