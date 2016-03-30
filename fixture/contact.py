from model.contact import Contact
import re
import random
import jsonpickle
import os.path
# import time
from selenium.webdriver.support.ui import Select

f = "data/context.json"


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.app.click_home()
            # self.app.go_to_home()
            # self.app.open_home_page()
            self.contact_cache = []
            for element in wd.find_elements_by_name("entry"):
                cells = element.find_elements_by_tag_name("td")
                first_name = cells[2].text
                last_name = cells[1].text
                id = cells[0].find_element_by_tag_name("input").get_attribute("value")
                # For Backward verification
                all_phones = cells[5].text
                all_emails = cells[4].text
                address = cells[3].text
                self.contact_cache.append(Contact(id=id,
                                                  first_name=first_name,
                                                  last_name=last_name,
                                                  address=address,
                                                  all_emails=all_emails,
                                                  all_phones_from_home_page=all_phones
                                                  ))
                # For Direct verification
                # all_phones = cells[5].text.splitlines()
                # self.contact_cache.append(Contact(id=id, first_name=first_name, last_name=last_name,
                #                                   home_phone=all_phones[0], mobile_phone=all_phones[1],
                #                                   work_phone=all_phones[2], phone_2=all_phones[3]))
                # self.contact_cache.append(Contact(id=id, first_name=first_name, last_name=last_name))
        return list(self.contact_cache)

    def fill_contact_form(self, wd, contact):
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.first_name)
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(contact.middle_name)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.last_name)
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(contact.nick_name)
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys(contact.title)
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(contact.company)
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(contact.address)
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(contact.home_phone)
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(contact.mobile_phone)
        wd.find_element_by_name("work").click()
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys(contact.work_phone)
        wd.find_element_by_name("fax").click()
        wd.find_element_by_name("fax").clear()
        wd.find_element_by_name("fax").send_keys(contact.fax_phone)
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(contact.email_1)
        wd.find_element_by_name("email2").click()
        wd.find_element_by_name("email2").clear()
        wd.find_element_by_name("email2").send_keys(contact.email_2)
        wd.find_element_by_name("email3").click()
        wd.find_element_by_name("email3").clear()
        wd.find_element_by_name("email3").send_keys(contact.email_3)
        wd.find_element_by_name("homepage").click()
        wd.find_element_by_name("homepage").clear()
        wd.find_element_by_name("homepage").send_keys(contact.homepage)
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[14]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[14]").click()
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[7]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[7]").click()
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys(contact.birthday_year)
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[3]//option[9]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[3]//option[9]").click()
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[4]//option[10]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[4]//option[10]").click()
        wd.find_element_by_name("ayear").click()
        wd.find_element_by_name("ayear").clear()
        wd.find_element_by_name("ayear").send_keys(contact.anniversary_year)
        # if not wd.find_element_by_xpath("//div[@id='content']/form/select[5]//option[4]").is_selected():
        #     wd.find_element_by_xpath("//div[@id='content']/form/select[5]//option[4]").click()
        wd.find_element_by_name("address2").click()
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys(contact.address_2)
        wd.find_element_by_name("phone2").click()
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys(contact.phone_2)
        wd.find_element_by_name("notes").click()
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys(contact.notes)

    def add(self, contact):
        wd = self.app.wd
        # init contact creation
        wd.find_element_by_link_text("add new").click()
        # fill contact form
        self.fill_contact_form(wd, contact)
        # submit contact creation
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.app.click_home
        self.contact_cache = None

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.app.go_to_home()
        wd.find_elements_by_name("selected[]")[index].click()
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        self.contact_cache = None

    def delete_contact_by_id(self, id):
        wd = self.app.wd
        self.app.go_to_home()
        # wd.find_elements_by_name("selected[]")[index].click()
        self.select_contact_by_id(id)
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        self.app.go_to_home()
        self.contact_cache = None

    def select_contact_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_xpath("//input[@id='%s']" % id).click()
        # wd.find_element_by_xpath("//input[@id='121']").click()

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def modify_contact_by_index(self, index, contact):
        wd = self.app.wd
        # init contact modification
        wd.find_elements_by_xpath("//img[@alt='Edit']")[index].click()
        # fill form with new values
        self.fill_contact_form(wd, contact)
        # submit modification
        wd.find_element_by_xpath("//input[@name='update']").click()
        wd.find_element_by_link_text("home").click()
        self.contact_cache = None

    def modify_contact_by_id(self, contact, id):
        wd = self.app.wd
        self.app.go_to_home()
        wd.find_element_by_xpath("//a[@href='edit.php?id=%s']/img" % id).click()
        self.fill_contact_form(wd, contact)
        # submit modification
        wd.find_element_by_xpath("//input[@name='update']").click()
        wd.find_element_by_link_text("home").click()
        self.contact_cache = None

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.app.go_to_home()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.app.go_to_home()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def modify_first_contact(self, contact):
        self.modify_contact_by_index(0, contact)

    def count(self):
        wd = self.app.wd
        self.app.click_home()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        first_name = wd.find_element_by_name("firstname").get_attribute("value")
        # first_name = wd.find_element_by_xpath("//input[@name='firstname']").text
        last_name = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        home_phone = wd.find_element_by_name("home").get_attribute("value")
        work_phone = wd.find_element_by_name("work").get_attribute("value")
        mobile_phone = wd.find_element_by_name("mobile").get_attribute("value")
        phone_2 = wd.find_element_by_name("phone2").get_attribute("value")
        email_1 = wd.find_element_by_name("email").get_attribute("value")
        email_2 = wd.find_element_by_name("email2").get_attribute("value")
        email_3 = wd.find_element_by_name("email3").get_attribute("value")
        return Contact(id=id,
                       first_name=first_name,
                       last_name=last_name,
                       address=address,
                       home_phone=home_phone,
                       mobile_phone=mobile_phone,
                       work_phone=work_phone,
                       phone_2=phone_2,
                       email_1=email_1,
                       email_2=email_2,
                       email_3=email_3)

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        home_phone = re.search("H: (.*)", text).group(1)
        work_phone = re.search("W: (.*)", text).group(1)
        mobile_phone = re.search("M: (.*)", text).group(1)
        phone_2 = re.search("P: (.*)", text).group(1)
        return Contact(home_phone=home_phone,
                       mobile_phone=mobile_phone,
                       work_phone=work_phone,
                       phone_2=phone_2
                       )

    def add_contact_to_group(self, id):
        context = {}
        wd = self.app.wd
        self.select_contact_by_id(id)
        wd.find_element_by_xpath("//select[@name='to_group']").click()
        l = list(wd.find_elements_by_xpath("//select[@name='to_group']/option"))
        selected_group = random.choice(l)
        selected_group.click()
        context['selected_group_name'] = selected_group.text
        context['selected_contact_id'] = id
        file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)
        with open(file, "w") as out:
            jsonpickle.set_encoder_options("json", indent=2)
            out.write(jsonpickle.encode(context))
        wd.find_element_by_xpath("//input[@name='add']").click()
        self.app.click_home()

    def delete_contact_from_group(self, contact_id, group_name):
        wd = self.app.wd
        Select(wd.find_element_by_xpath("//select[@name='group']")).select_by_visible_text(group_name)
        # time.sleep(2)
        wd.find_element_by_xpath("//input[@id='%s']" % contact_id).click()
        wd.find_element_by_css_selector(".left input[name='remove']").click()
