class Customer:
    """ Class to manage customer details """

    def __init__(self, customer_id, name, telephone_number, email):
        self.customer_id = customer_id
        self._name = name
        self._telephone_number = telephone_number
        self._email = email
        self.appointment_history = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name.title()

    @property
    def telephone_number(self):
        return self._telephone_number

    @telephone_number.setter
    def telephone_number(self, telephone_number):
        self._telephone_number = f'({telephone_number[:3]}) {telephone_number[3:6]}-{telephone_number[-4:]}'

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        self._email = email

    def __str__(self):
        return f'Customer: {self.name} (ID: {self.customer_id})'

