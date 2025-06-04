from models.fulltimeemployee import FullTimeEmployee
from models.employee import Employee
from exceptions.negativenumberexception import NegativeNumberException
from faker import Faker
#create objects of Employee class
#constructor overloading
#abstarct class cannot be instantiated
#employee=Employee("Parameswari")
#print(employee.get_name())
fake= Faker("en_IN")  # Initialize Faker with Hindi locale
for _ in range(0, 5):
   
   try:
    #objects are staored in heap memory
    employee=FullTimeEmployee(fake.random_int(min=1000, max=9999),
        fake.name(),
        fake.job(),
        fake.random_int(min=30000, max=120000),
        fake.email(),
        fake.phone_number(), fake.random_int(min=3000, max=10000))
   except NegativeNumberException as e:
    print(f"Error: {e.message} Value: {e.value}") 
   except Exception as e:
    print(f"An unexpected error occurred: {e}")
   else:
    employee.set_id(4677)
    print(employee.get_name())
    print(f"Computed Salary: {employee.calculate_salary()}")
    employee.email="parameswari@gmail.com"
    print(employee.email)
    #static variable is stored in method area at class level
    print(f"Number of people salary calculated: {Employee.employeeCount}")
    Employee.notify(employee)
   finally:
        print("Execution completed.")