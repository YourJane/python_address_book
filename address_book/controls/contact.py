class Contact:

    def __init__(self, name, last_name, phone, social_account, city, **kwargs):
        self.name = name
        self.last_name = last_name
        self.phone = phone
        self.social_account = social_account
        self.city = city
        self.address_street = kwargs.get('address_street')
        self.second_name = kwargs.get('second_name')
        self.email = kwargs.get("email")

