class Service:
    """Class to manager barbershop services"""

    def __init__(self, service_id, name, description, price, duration):
        self.service_id = service_id
        self.name = name
        self.description = description
        self.price = price
        self.duration = duration