# -*- coding: utf-8 -*-
from model.contact import Contact
import random
import string

constant = [
    Contact(first_name="", middle_name="", last_name=""),
    Contact(first_name="First", middle_name="Firstovich", last_name="Firstoff"),
    Contact(first_name="Second", middle_name="Secondovich", last_name="Secondoff")
]


def random_string(prefix, maxlen):
    # symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    # symbols = string.ascii_letters + string.digits + " "*10
    # symbols = string.ascii_letters
    symbols = string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [
        Contact(first_name=random_string("name", 10),
                middle_name=random_string("middleName", 10),
                last_name=random_string("lastName", 10),
                nick_name=random_string("nickName", 10),
                title=random_string("title", 10),
                company=random_string("company", 10),
                address=random_string("address", 10),
                home_phone=random_string("homePhone", 10),
                mobile_phone=random_string("mobilePhone", 10),
                work_phone=random_string("workPhone", 10),
                fax_phone=random_string("faxPhone", 10),
                email_1=random_string("email1@company", 10),
                email_2=random_string("email2@company.com", 10),
                email_3=random_string("email3@company.com", 10),
                homepage=random_string("www.homepage.com", 10),
                birthday_year=random_string("2000", 10),
                anniversary_year=random_string("2005", 10),
                address_2=random_string("address", 10),
                phone_2=random_string("home", 10),
                notes=random_string("notes", 10)
                )
        for i in range(5)
    ]
