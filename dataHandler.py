import csv

from customer import Customer
from employee import Employee

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