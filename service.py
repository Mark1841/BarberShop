class Service:
    """Class to manager barbershop services"""

    def __init__(self, service_id, name, description, price, duration):
        self.service_id = service_id
        self.name = name
        self.description = description
        self.price = price
        self.duration = int(duration)


    def to_csv_row(self):
        return [
            self.service_id,
            self.name,
            self.description,
            self.price,
            self.duration
        ]
    
    @staticmethod
    def from_csv(row):
        service_id, name, description, price, duration = row
        return Service(service_id, name, description, price, int(duration))