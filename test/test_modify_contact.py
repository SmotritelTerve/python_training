# -*- coding: utf-8 -*-
from model.contact import Contact


def test_modify_first_contact(app):
    random_value = str(app.get_random_int())
    if app.contact.count() == 0:
        app.contact.add(Contact(first_name="First Contact"))
    old_contacts = app.contact.get_contact_list()
    contact = Contact(first_name="name" + random_value,
                      middle_name="middleName" + random_value,
                      last_name="lastName" + random_value,
                      nick_name="nickName" + random_value,
                      title="title" + random_value,
                      company="company" + random_value,
                      address="address" + random_value,
                      home_phone="homePhone" + random_value,
                      mobile_phone="mobilePhone" + random_value,
                      work_phone="workPhone" + random_value,
                      fax_phone="faxPhone" + random_value,
                      email_1="email1@company" + random_value + ".com",
                      email_2="email2@company" + random_value + ".com",
                      email_3="email3@company" + random_value + ".com",
                      homepage="www.homepage" + random_value + ".com",
                      birthday_year=random_value,
                      anniversary_year=random_value,
                      address_2="address" + random_value,
                      phone_2="home" + random_value,
                      notes="notes" + random_value)

    # contact.id = old_contacts[0].id
    # app.contact.modify_first_contact(contact)
    # new_contacts = app.contact.get_contact_list()
    # assert len(old_contacts) == len(new_contacts)
    # old_contacts[0] = contact
    # assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

    contact.id = old_contacts[0].id
    app.contact.modify_first_contact(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact
    # assert old_contacts == new_contacts
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
