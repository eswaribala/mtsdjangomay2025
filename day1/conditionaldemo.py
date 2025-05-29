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
elif( employeeGender.value == 2):
    print("Employee is FEMALE")
else:
    print("Employee is OTHER")