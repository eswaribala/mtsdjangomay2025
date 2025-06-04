from datetime import datetime
from faker import Faker
fake= Faker("en_IN")  # Initialize Faker with Hindi locale
from models.employee import Employee
employees= []

for _ in  range(1,10):
    
    employee=Employee(
        fake.random_int(min=1000, max=9999),
        fake.name(),
        fake.job(),
        fake.random_int(min=30000, max=120000),
        fake.email(),
        fake.phone_number()
       
    )
    employees.append(employee)
sorted_employees = sorted(employees, key=lambda x: x.get_name(), reverse=False)
for employee in sorted_employees:  
    print(f"Id: {employee.get_id()}, Name: {employee.get_name()}, Designation: {employee.get_designation()}, Salary: {employee.get_salary()}, Email: {employee.email}, Phone: {employee.get_contact_no()}")
    print(f"Details: {employee.get_details()}")
#sort the list of objects
