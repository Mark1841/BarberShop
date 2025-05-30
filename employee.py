class Employee:
    """Class to manage the store employees"""

    def __init__(self, employee_id, name, telephone_number, active):
        self.employee_id = employee_id
        self.name = name
        self.telephone_number = telephone_number
        self.active = active

    def __str__(self):
        return f'{self.name}'