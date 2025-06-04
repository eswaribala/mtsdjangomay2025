import csv
import os
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

dirPath="E:\\MTSTraningmay2025\\day1\\reports"
if not os.path.exists(dirPath):
    os.makedirs(dirPath)
filePath=os.path.join(dirPath, f"employee_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv")
try:
    with open(filePath, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        # Write the header
        writer.writerow(["Id", "Name", "Designation", "Salary", "Email", "Phone"])
        
        # Write the employee data
        for employee in sorted_employees:  
            writer.writerow([
                employee.get_id(),
                employee.get_name(),
                employee.get_designation(),
                employee.get_salary(),
                employee.email,
                employee.get_contact_no()
            ])
except FileNotFoundError as e:
    print(f"Error: The file path {filePath} does not exist. Please check the directory.")
except Exception as e:
    print(f"An error occurred while writing to the CSV file: {e}")
else:
    print(f"CSV file created successfully at {filePath}")