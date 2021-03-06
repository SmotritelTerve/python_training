from sys import maxsize


class Contact:

    def __init__(self, first_name="John", middle_name="Fitz", last_name="Doe", nick_name="Johnny", title="Comrade",
                 company="West Coast Gang", address="Loosers Street, 13", home_phone="666777333", mobile_phone="+16667778888",
                 work_phone="777", fax_phone="000", email_1="email_1@example.com", email_2="email_2@example.com",
                 email_3="email_3@example.com", homepage="habrahabr.ru", birthday_year="2000", anniversary_year="2005",
                 address_2="Lucky Street, 7", phone_2="666666666", notes="do not worry, be happy", id=None,
                 all_phones_from_home_page=None, all_emails=None):
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.nick_name = nick_name
        self.title = title
        self.company = company
        self.address = address
        self.home_phone = home_phone
        self.mobile_phone = mobile_phone
        self.work_phone = work_phone
        self.fax_phone = fax_phone
        self.email_1 = email_1
        self.email_2 = email_2
        self.email_3 = email_3
        self.homepage = homepage
        self.birthday_year = birthday_year
        self.anniversary_year = anniversary_year
        self.address_2 = address_2
        self.phone_2 = phone_2
        self.notes = notes
        self.all_phones_from_home_page = all_phones_from_home_page
        self.all_emails = all_emails
        self.id = id

    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.first_name, self.last_name)

    def __eq__(self, other):
        # return self.id == other.id and self.last_name == other.last_name
        return (self.id is None or other.id is None or self.id == other.id) and self.first_name == other.first_name\
               and self.last_name == other.last_name

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
