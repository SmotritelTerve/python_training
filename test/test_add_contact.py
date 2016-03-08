# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
# from data.contacts import constant as testdata
from data.contacts import testdata


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

