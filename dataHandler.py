import csv
from datetime import datetime

from customer import Customer
from employee import Employee
from appointment import Appointment
from service import Service 

# Customer CSV Functions

def save_customers(customers, filename="customers.csv"):
    with open(filename, mode="w", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["CustomerID", "Name", "TelephoneNumber", "Email"])

        for c in customers:
            writer.writerow(c.to_csv_row())

def load_customers(filename="customers.csv"):
    customers = []

    try:
        with open(filename, mode="r") as file:
            reader = csv.reader(file)

            # Skips the header of the CSV
            next(reader)
            for r in reader:
                customers.append(Customer.from_csv(r))
    except FileNotFoundError:
        print(f"{filename} not found!")

    return customers

# Employee CSV Functions

def save_employees(employees, filename="employees.csv"):
    with open(filename, mode="w", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["EmployeeID", "Name", "TelephoneNumber", "Active"])

        for e in employees:
            writer.writerow(e.to_csv_row())

def load_employees(filename="employees.csv"):
    employees = []

    try:
        with open(filename, mode="r") as file:
            reader = csv.reader(file)

            # Skips the header of the CSV
            next(reader)
            for r in reader:
                employees.append(Employee.from_csv(r))
    except FileNotFoundError:
        print(f"{filename} not found!")

    return employees

def save_appointments(appointments, filename="appointments.csv"):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Customer', 'Service', 'Employee', 'Date', 'Status'])
    
        for a in appointments:
            writer.writerow(a.to_csv_row())

def load_appointments(customers, services, employees, filename="appointments.csv"):
    appointments = []

    try:
        with open(filename, mode='r') as file:
            reader = csv.reader(file)

            next(reader)
            for r in reader:
                appointments.append(Appointment.from_csv(r, customers, services, employees))
    except FileNotFoundError:
        print(f"{filename} not found!")

    return appointments

def save_services(services, filename="services.csv"):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Service_ID', 'Name', 'Description', 'Price', 'Duration'])
    
        for s in services:
            writer.writerow(s.to_csv_row())

def load_services(filename="services.csv"):
    services = []

    try:
        with open(filename, mode='r') as file:
            reader = csv.reader(file)

            next(reader)
            for r in reader:
                services.append(Service.from_csv(r))
    except FileNotFoundError:
        print(f"{filename} not found!")

    return services