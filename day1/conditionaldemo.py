from enum import Enum
from faker import Faker
import random
class Gender(Enum):
    MALE=1
    FEMALE=2
    OTHER=3

fake=Faker()
employeeGender=random.choice(list(Gender))
employeeSalary=fake.random_int(min=300000, max=6000000)
print(f"Employee{employeeGender.value} earns {employeeSalary} per annum")

if( employeeGender.value == 1):
    print("Employee is MALE")
    if( employeeSalary <= 500000):
        print("No Tax")
    elif( employeeSalary >= 500001) and (employeeSalary <= 2000000):
        print(f"Tax is 10%={employeeSalary * 0.1}")
    elif( employeeSalary >= 2000001) and (employeeSalary <= 3000000):
        print(f"Tax is 20%={employeeSalary * 0.2}")
    else:
        print(f"Tax is 30%={employeeSalary * 0.3}")
elif( employeeGender.value == 2):
    print("Employee is FEMALE")
    if( employeeSalary <= 800000):
        print("No Tax")
    elif( employeeSalary >= 800001) and (employeeSalary <= 2500000):
        print(f"Tax is 10%={employeeSalary * 0.1}")
    elif( employeeSalary >= 2500001) and (employeeSalary <= 4000000):
        print(f"Tax is 20%={employeeSalary * 0.2}")
    else:
        print(f"Tax is 30%={employeeSalary * 0.3}")
else:
    print("Employee is OTHER")
    if( employeeSalary <= 1000000):
        print("No Tax")
    elif( employeeSalary >= 1000001) and (employeeSalary <= 3000000):
        print(f"Tax is 10%={employeeSalary * 0.1}")
    elif( employeeSalary >= 3000001) and (employeeSalary <= 5000000):
        print(f"Tax is 20%={employeeSalary * 0.2}")
    else:
        print(f"Tax is 30%={employeeSalary * 0.3}")