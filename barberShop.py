class BarberShop:
    """ Class to manage the day to day operations at the store"""

    def __init__(self, name):
        self.name = name # Name of the barber shop
        self.customers = []
        self.services = []
        self.employees = []
        self.appointments = []



    def add_customer(self, customer):
        self.customers.append(customer)

    def add_service(self, service):
        self.services.append(service)

    def add_employee(self, employee):
        self.employees.append(employee)

    def add_appointment(self, appointment):
        self.appointments.append(appointment)