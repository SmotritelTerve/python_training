import mysql.connector
from model.group import Group
from model.contact import Contact


class DbFixture:

    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = mysql.connector.connect(host=host, database=name, user=user, password=password)
        self.connection.autocommit = True

    def get_group_list(self):
        list=[]
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (id, name, header, footer) = row
                list.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return list

    def get_contact_list(self):
        list=[]
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, lastname, address from addressbook WHERE deprecated = '0000-00-00 00:00:00'")
            for row in cursor:
                (id, first_name, last_name, address) = row
                list.append(Contact(id=str(id), first_name=first_name, last_name=last_name, address=address))
        finally:
            cursor.close()
        return list

    def get_group_id_by_name(self, group_name):
        cursor = self.connection.cursor()
        try:
            cursor.execute("SELECT group_id FROM `group_list` WHERE group_name = %s" % "'" + group_name + "'")
            for row in cursor:
                group_id = row
        finally:
            cursor.close()
        return group_id

    def get_contacts_in_group(self, group_id):
        list=[]
        cursor = self.connection.cursor()
        try:
            cursor.execute("SELECT id FROM `address_in_groups` WHERE group_id = %d" % int(group_id))
            for row in cursor:
                id = row
                list.append(id[0])
        finally:
            cursor.close()
        return list


    def destroy(self):
        self.connection.close()
