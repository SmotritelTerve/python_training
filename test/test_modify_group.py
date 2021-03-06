# -*- coding: utf-8 -*-
from model.group import Group
from random import randrange


# def test_modify_first_group(app):
#     random_value = str(app.get_random_int())
#     if app.group.count() == 0:
#         app.group.create(Group(name="First group", header="First header", footer="First footer"))
#     old_groups = app.group.get_group_list()
#     app.group.modify_first_group(Group(name="group" + random_value, header="header" + random_value,
#                                        footer="footer" + random_value))
#     new_groups = app.group.get_group_list()
#     assert len(old_groups) == len(new_groups)


def test_modify_group_name(app, db, check_ui):
    random_value = str(app.get_random_int())
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="First group", header="First header", footer="First footer"))
    # old_groups = app.group.get_group_list()
    old_groups = db.get_group_list()
    index = randrange(len(old_groups))
    group = Group(name="New group" + random_value)
    group.id = old_groups[index].id
    app.group.modify_group_by_index(index, group)
    new_groups = db.get_group_list()
    assert len(old_groups) == len(new_groups)

    def clean(group):
        return Group(id=group.id, name=group.name.strip())
    new_groups = map(clean, db.get_group_list())
    new_groups_1 = map(clean, app.group.get_group_list())
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(new_groups_1, key=Group.id_or_max)


# def test_modify_group_header(app):
#     if app.group.count() == 0:
#         app.group.create(Group(name="First group", header="First header", footer="First footer"))
#     old_groups = app.group.get_group_list()
#     app.group.modify_first_group(Group(header="New header"))
#     new_groups = app.group.get_group_list()
#     assert len(old_groups) == len(new_groups)
