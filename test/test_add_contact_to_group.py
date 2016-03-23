from model.group import Group
from model.contact import Contact
import random
import json
import os.path


def test_add_contact_to_group(app, db):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="First group", header="First header", footer="First footer"))
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(first_name="First Contact"))
    contacts = db.get_contact_list()
    contact = random.choice(contacts)
    app.contact.add_contact_to_group(contact.id)
    context_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data\\context.json")
    with open(context_file) as f:
        context = json.load(f)
    group_id = db.get_group_id_by_name(context["selected_group_name"])
    l = db.get_contacts_in_group(group_id[0])
    assert str(contact.id) in str(l)
