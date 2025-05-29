from datetime import datetime
from faker import Faker
fake= Faker("hi_IN")  # Initialize Faker with Hindi locale
from models.employee import Employee
employees= (Employee(
        fake.random_int(min=1000, max=9999),
        fake.name(),
        fake.job(),
        fake.random_int(min=30000, max=120000),
        fake.email(),
        fake.phone_number()
       
    ),Employee(
        fake.random_int(min=1000, max=9999),
        fake.name(),
        fake.job(),
        fake.random_int(min=30000, max=120000),
        fake.email(),
        fake.phone_number()
       
    ),Employee(
        fake.random_int(min=1000, max=9999),
        fake.name(),
        fake.job(),
        fake.random_int(min=30000, max=120000),
        fake.email(),
        fake.phone_number()
       
    ))


for employee in employees:  
    print(f"Id: {employee.get_id()}, Name: {employee.get_name()}, Designation: {employee.get_designation()}, Salary: {employee.get_salary()}, Email: {employee.get_email()}, Phone: {employee.get_contact_no()}")
    print(f"Details: {employee.get_details()}")
#sort the list of objects

