from faker import Faker
fake=Faker()
employeeId=fake.random_int(min=1000, max=9999)
employeeName=fake.name()
employeeSalary=fake.random_int(min=30000, max=120000)  
print(f"Employee ID: {employeeId} \nEmployee Name: {employeeName} \nEmployee Salary: {employeeSalary}") 