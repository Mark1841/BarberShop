from customer import Customer
from employee import Employee
from service import Service

from datetime import datetime

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

    def to_csv_row(self):
        return [
            self.customer.name,
            self.service.service_id,
            self.employee.name,
            self.date.strftime("%Y-%m-%d %H:%M"),
            self.status,
            ]

    # @staticmethod means the method does not require access to the class
    # So no self needed here
    @staticmethod
    def from_csv(row, customers, services, employees):
        customer, service, employee, date, status = row
        customer = next((c for c in customers if c.name == customer), None)
        service = next((s for s in services if str(s.service_id) == service), None)
        employee = next((e for e in employees if e.name == employee), None)
        date = datetime.strptime(date, "%Y-%m-%d %H:%M")

        return Appointment(customer, service, employee, date, status)

    def __str__(self):
        return f'{self.customer}, Service: {self.service} Staff Member: {self.employee}, Date: {self.date})'

