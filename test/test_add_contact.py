# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import random
import string


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
        for i in range(5)
    ]


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.add(contact)
    # new_contacts = app.contact.get_contact_list()
    # assert len(old_contacts) + 1 == len(new_contacts)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_add_contact_old_way(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(first_name="name", middle_name="middleName", last_name="lastName", nick_name="nickName",
                      title="title", company="company", address="address", home_phone="homePhone",
                      mobile_phone="mobilePhone", work_phone="workPhone", fax_phone="faxPhone",
                      email_1="email1@company", email_2="email2@company.com", email_3="email3@company.com",
                      homepage="www.homepage.com", birthday_year="2000", anniversary_year="2005",
                      address_2="address", phone_2="home", notes="notes")
    app.contact.add(contact)
    # new_contacts = app.contact.get_contact_list()
    # assert len(old_contacts) + 1 == len(new_contacts)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

