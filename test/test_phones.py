import re


def test_phones_on_home_page(app):
    contact_from_home_page = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    # For Backward verification
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)
    # For Direct verification
    # assert contact_from_home_page.home_phone == clear(contact_from_edit_page.home_phone)
    # assert contact_from_home_page.work_phone == clear(contact_from_edit_page.work_phone)
    # assert contact_from_home_page.mobile_phone == clear(contact_from_edit_page.mobile_phone)
    # assert contact_from_home_page.phone_2 == clear(contact_from_edit_page.phone_2)


def test_phones_on_contact_view_page(app):
    contact_from_view_page = app.contact.get_contact_from_view_page(0)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_view_page.home_phone == contact_from_edit_page.home_phone
    assert contact_from_view_page.mobile_phone == contact_from_edit_page.mobile_phone
    assert contact_from_view_page.work_phone == contact_from_edit_page.work_phone
    assert contact_from_view_page.phone_2 == contact_from_edit_page.phone_2


def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.home_phone, contact.mobile_phone, contact.work_phone, contact.phone_2]
                                       ))))


def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                     filter(lambda x: x is not None,
                            [contact.email_1, contact.email_2, contact.email_3])))

