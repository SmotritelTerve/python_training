# -*- coding: utf-8 -*-
import pytest
from fixture.application import Application
from model.contact import Contact


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.login(username="admin", password="secret")
    app.add_contact(Contact(name="name", middle_name="middleName", last_name="lastName", nick_name="nickName",
                                 title="title", company="company", address="address", home_phone="homePhone",
                                 mobile_phone="mobilePhone", work_phone="workPhone", fax_phone="faxPhone",
                                 email_1="email1@company", email_2="email2@company.com", email_3="email3@company.com",
                                 homepage="www.homepage.com", birthday_year="2000", anniversary_year="2005",
                                 address_2="address", phone_2="home", notes="notes"))
    app.logout()


