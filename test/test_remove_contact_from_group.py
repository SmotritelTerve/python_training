import json
import os.path


# NOTE: test_add_contact_to_group should be run first
def test_remove_contact_from_group(app, db):
    context_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data\\context.json")
    with open(context_file) as f:
        context = json.load(f)
    app.contact.delete_contact_from_group(context["selected_contact_id"], context["selected_group_name"])
    group_id = db.get_group_id_by_name(context["selected_group_name"])
    l = db.get_contacts_in_group(group_id[0])
    assert str(context["selected_contact_id"]) not in str(l)

