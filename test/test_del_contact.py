# -*- coding: utf-8 -*-
from model.contact import Contact
# from random import randrange
import random


def test_delete_some_contact(app, db, check_ui):

    if len(db.get_contact_list()) == 0:
        app.contact.add(Contact(first_name="First Contact"))

    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    app.contact.delete_contact_by_id(contact.id)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts.remove(contact)
    assert old_contacts == new_contacts

    def clean(contact):
        return Contact(id=contact.id, first_name=contact.first_name.strip())
    new_contacts = map(clean, db.get_contact_list())
    new_contacts_1 = map(clean, app.contact.get_contact_list())

    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(new_contacts_1,
                                                                     key=Contact.id_or_max)



