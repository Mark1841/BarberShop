class Appointment:
    """Class to manage appointments"""

    def __init__(self, customer, employee, date, status):
        self.customer = customer
        self.employee = employee
        self.date = date
        self._status = status

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, status):
        print("setter was called")
        if status in ['Booked', 'Completed', 'Cancelled']:
            self._status = status

