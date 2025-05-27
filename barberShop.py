class BarberShop:
    """ Class to manage the day to day operations at the store"""

    def __init__(self, name):
        self.name = name
        self.customers = {}
        self.services = {}


    def add_customer(self, customer):
        self.customers[customer.customer_id] = customer

    def add_service(self, service):
        self.services[service.customer_id] = service
