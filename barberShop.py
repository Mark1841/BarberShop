from appointment import Appointment
from customer import Customer
from employee import Employee
from service import Service
from dataHandler import load_customers, load_employees, load_appointments, load_services
from datetime import datetime, timedelta

class BarberShop:
    """ Class to manage the day-to-day operations at the store"""

    def __init__(self, name):
        self.name = name # Name of the barber shop
        self.customers = load_customers()
        self.services = load_services()
        self.employees = load_employees()
        self.appointments = load_appointments(self.customers, self.services, self.employees)

    def find_customer(self, name):
        """ Finds a customer by name"""
        for customer in self.customers:
            if customer.name == name.title():
                print(f'found customer: {customer}')
                return customer
        return None

    def find_service(self, name):
        """ Finds a customer by name"""
        for service in self.services:
            if service.name == name:
               return service
        return None

    def find_employee(self, name):
        """ Finds an employee by name"""
        for employee in self.employees:
            if employee.name == name.title():
               return employee
        return None

    def add_customer(self, name = None):
        """ Adds a customer to the shop """
        customer_id = len(self.customers) + 1
        if name is None:
            name = input('Enter customer name: ')
        telephone_number = input('Enter customer phone number: ')
        email = input('Enter customer email: ')
        new_customer = Customer(customer_id, name, telephone_number, email)
        self.customers.append(new_customer)

    def add_employee(self, name = None):
        """ Adds an employee to the shop """
        employee_id = len(self.employees) + 1
        if name is None:
            name = input('Enter employee name: ')
        telephone_number = input('Enter employee phone number: ')
        new_employee = Employee(employee_id, name, telephone_number, True)
        self.employees.append(new_employee)

    def add_service(self, name = None):
        """ Adds a service to the shop """
        service_id = len(self.services) + 1
        if name is None:
            name = input('Enter service name: ')
        description = input('Enter service description: ')
        price = input('Enter service price: ')
        duration = input('Enter service duration: ')
        new_service = Service(service_id, name, description, price, int(duration))
        self.services.append(new_service)

    def add_appointment(self):
        """ Adds an appointment to the shop """
        customer_name = input('Enter customers name: ')
        customer = self.find_customer(customer_name)
        if customer is None:
            print('Customer not found, they will need to be added to database!')
            self.add_customer(customer_name)
            customer = self.find_customer(customer_name)

        service_name = input('Enter the service the customer wants: ')
        service = self.find_service(service_name)
        if service is None:
            print('Service not found, it will need to be added to database!')
            self.add_service(service_name)
            service = self.find_service(service_name)
            
        employee_name = input('Enter the name of the employee completing the service: ')
        employee = self.find_employee(employee_name)
        if employee is None:
            print('Employee not found, they will need to be added to database!')
            self.add_employee(employee_name)
            employee = self.find_employee(employee_name)
        
        while True:
            # Calls get_valid_date to ensure the date is valid
            date = get_valid_date()

            # Current times being added at this moment
            new_start = date
            new_end = new_start + timedelta(minutes=int(service.duration))

            conflict = False
            for appointment in self.appointments:
                if appointment.employee == employee:
                    # Time that we are iterating through
                    start = appointment.date
                    print(type(appointment.service.duration))
                    end = start + timedelta(minutes=int(appointment.service.duration))
        
                    if (new_start < end and new_end > start):
                        print(f"ERROR: {employee.name} is already booked during this time.")
                        conflict = True
                        break
                    
            if not conflict:
                break
            else:
                choice = input("Would you like to (1) change the time or (2) choose a different employee?: ")

                if choice == '1':
                    print("Please enter a new date and time.")
                elif choice == '2':
                    while True:
                        employee_name = input('Enter the name of a different employee (or type "exit" to cancel): ')
                        if employee_name.lower() == "exit":
                            print("Appointment canceled.")
                            return

                        employee = self.find_employee(employee_name)
                        if employee is None:
                            print("Employee not found. Please enter a valid employee name or type 'exit' to cancel.")
                        else:
                            break


        status = "Booked"
        new_appointment = Appointment(customer, service, employee, date, status)
        (self.appointments.append(new_appointment))



def get_valid_date():
    while True:
        try:
            # Ask for input
            date = input('Enter the appointment date (Format: YYYY-MM-DD): ')
            time = input('Enter the appointment time (Format *24 Hour*: HH:MM): ')

            # We need to combine the date and time so it fits the datetime format
            # NOTE: datetime formate is 2025-06-05 14:30:00
            appointment_datetime = datetime.strptime(f"{date} {time}", "%Y-%m-%d %H:%M")
            
            if appointment_datetime <= datetime.now():
                print("ERROR: The appointment must be scheduled in the future. Please try again.")
                continue

            return appointment_datetime
        except ValueError:
            print("ERROR: Invalid date or time format. Please use the correct format (YYYY-MM-DD for date and HH:MM for time).")
        