class Employee:
    """Class to manage the store employees"""

    def __init__(self, employee_id, name, telephone_number, active):
        self.employee_id = employee_id
        self.name = name
        self.telephone_number = telephone_number
        self.active = active

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
        if telephone_number.isdigit():
            # Only format if it's all digits (e.g., "2896759388")
            self._telephone_number = f'({telephone_number[:3]}) {telephone_number[3:6]}-{telephone_number[-4:]}'
        else:
            # Already formatted, just store it
            self._telephone_number = telephone_number
            
    def to_csv_row(self):
        return [
            self.employee_id,
            self.name,
            self.telephone_number,
            self.active,
            ]

    # @staticmethod means the method does not require access to the class
    # So no self needed here
    @staticmethod
    def from_csv(row):
        employee_id, name, telephone_number, active = row
        customer = Employee(employee_id, name, telephone_number, active)
        return customer

    def __str__(self):
        return f'Employee: {self.name}, Telephone Number: {self._telephone_number} (ID: {self.employee_id})'