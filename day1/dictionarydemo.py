from faker import Faker

employeeDictionary = {}
fake=Faker()

employeeCount = int(input("Enter the number of employees: "))
for _ in range(employeeCount):
    key= fake.phone_number()  # Using phone number as key
    value=fake.name()
    employeeDictionary[key] = value

print("Employee Dictionary:")
for key, value in employeeDictionary.items():
    print(f"Key: {key}, Value: {value}")