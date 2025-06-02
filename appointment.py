class Appointment:
    """Class to manage appointments"""

    def __init__(self, customer, service, employee, date, status):
        self.customer = customer
        self.service = service
        self.employee = employee
        self.date = date
        self.status = status

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, status):
        print("setter was called")
        if status in ['Booked', 'Completed', 'Cancelled']:
            self._status = status

    def __str__(self):
        return f'Customer: {self.customer.name}, Service: {self.service.name} Staff Member: {self.employee.name}, Date: {self.date})'

