# -*- coding: utf-8 -*-
from model.contact import Contact
import random
import string
import os.path
# import json
import jsonpickle
import getopt
import sys

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of groups", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_string(prefix, maxlen):
    # symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    # symbols = string.ascii_letters + string.digits + " "*10
    # symbols = string.ascii_letters
    symbols = string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Contact(first_name="", middle_name="", last_name="")] + [
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
        for i in range(n)
    ]


file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    # out.write(json.dumps(testdata, default=lambda x: x.__dict__, indent=2))
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))

