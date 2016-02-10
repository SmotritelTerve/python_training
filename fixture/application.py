from selenium.webdriver.firefox.webdriver import WebDriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.contact import ContactHelper
import random


class Application:

    def __init__(self):
        self.wd = WebDriver()
        self.open_home_page()
        # self.wd.implicitly_wait(60)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost:8989/addressbook/")

    def get_random_int(self):
        return random.randrange(1, 2000)

    def destroy(self):
        self.wd.quit()
