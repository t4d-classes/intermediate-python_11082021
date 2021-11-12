

class Address:

    def __init__(self, street, city, state, zip):
        self.street = street
        self.city = city
        self.state = state
        self.zip = zip

    def mailing(self) -> str:
        return f"{self.street}\n{self.city}, {self.state} {self.zip}"


class PersonA:

    def __init__(self, first_name, last_name, street, city, state, zip):
        self.first_name = first_name
        self.last_name = last_name
        self.address = Address(street, city, state, zip)

    def full_name(self):
        return self.first_name + " " + self.last_name

    def mailing(self):
        return self.full_name() + "\n" + self.address.mailing()


class PersonB:

    def __init__(self, first_name, last_name, address):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address

    def full_name(self):
        return self.first_name + " " + self.last_name

    def mailing(self):
        return self.full_name() + "\n" + self.address.mailing()
