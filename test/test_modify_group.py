# -*- coding: utf-8 -*-
from model.group import Group


def test_modify_first_group(app):
    random_value = str(app.get_random_int())
    app.session.login(username="admin", password="secret")
    app.group.modify_first_group(Group(name="group" + random_value, header="header" + random_value,
                                       footer="footer" + random_value))
    app.session.logout()
