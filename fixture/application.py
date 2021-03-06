# from selenium.webdriver.firefox.webdriver import WebDriver
from selenium import webdriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.contact import ContactHelper
import random


class Application:

    def __init__(self, browser, base_url):
        # self.wd = WebDriver()
        if browser == "firefox":
            profile = webdriver.FirefoxProfile()
            profile.set_preference('browser.startup.homepage', '')
            profile.set_preference('startup.homepage_welcome_url', '')
            profile.set_preference('startup.homepage_welcome_url.additional', '')
            self.wd = webdriver.Firefox(profile)
        elif browser == "chrome":
            options = webdriver.ChromeOptions()
            options.add_experimental_option("excludeSwitches", ["ignore-certificate-errors"])
            options.add_argument('--disable-extensions')
            self.wd = webdriver.Chrome(chrome_options=options)
        elif browser == "ie":
            self.wd = webdriver.Ie()
        else:
            raise ValueError("Unrecognized browser %s" % browser)

        # self.wd.implicitly_wait(60)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)
        self.base_url = base_url
        self.open_home_page()

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def open_home_page(self):
        wd = self.wd
        wd.get(self.base_url)

    def go_to_home(self):
        wd = self.wd
        if not (wd.current_url.endswith("/addressbook/")):
            wd.find_element_by_link_text("home").click()

    def get_random_int(self):
        return random.randrange(1, 2000)

    def destroy(self):
        self.wd.quit()

    def click_home(self):
        wd = self.wd
        wd.find_element_by_link_text("home").click()
