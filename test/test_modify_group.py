# -*- coding: utf-8 -*-
from model.group import Group


def test_modify_first_group(app):
    random_value = str(app.get_random_int())
    app.session.login(username="admin", password="secret")
    app.group.modify_first_group(Group(name="group" + random_value, header="header" + random_value,
                                       footer="footer" + random_value))
    app.session.logout()


def test_modify_group_name(app):
    app.session.login(username="admin", password="secret")
    app.group.modify_first_group(Group(name="New group"))
    app.session.logout()


def test_modify_group_header(app):
    app.session.login(username="admin", password="secret")
    app.group.modify_first_group(Group(header="New header"))
    app.session.logout()
