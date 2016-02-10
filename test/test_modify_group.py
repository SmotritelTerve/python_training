# -*- coding: utf-8 -*-
from model.group import Group


def test_modify_first_group(app):
    random_value = str(app.get_random_int())
    if app.group.count() == 0:
        app.group.create(Group(name="First group", header="First header", footer="First footer"))
    app.group.modify_first_group(Group(name="group" + random_value, header="header" + random_value,
                                       footer="footer" + random_value))


def test_modify_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="First group", header="First header", footer="First footer"))
    app.group.modify_first_group(Group(name="New group"))


def test_modify_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(name="First group", header="First header", footer="First footer"))
    app.group.modify_first_group(Group(header="New header"))
