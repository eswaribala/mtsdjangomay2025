from faker import Faker
fake=Faker()
employeeId=fake.random_int(min=1000, max=9999)
employeeName=fake.name()
employeeSalary=fake.random_number(digits=6, fix_len=True)  
print(f"Employee ID: {employeeId} \nEmployee Name: {employeeName} \nEmployee Salary: {employeeSalary}") 
da=fake.pyfloat(left_digits=2, right_digits=2, positive=True) * employeeSalary
print(f"DA Amount: {da}")
#complex number
complexNumber=complex(fake.random_int(min=1, max=10), fake.random_int(min=1, max=10))
print(f"Complex Number: {complexNumber}")
#binary number
binaryNumber=bin(fake.random_int(min=1, max=10))
print(f"Binary Number: {binaryNumber}")
#octal number
octalNumber=oct(fake.random_int(min=1, max=10))
print(f"Octal Number: {octalNumber}")   
#hexadecimal number
hexadecimalNumber=hex(fake.random_int(min=1, max=10))
print(f"Hexadecimal Number: {hexadecimalNumber}")



