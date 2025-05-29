from datetime import datetime
from faker import Faker

for _ in  range(1,10):
    
    #type casting
    index=_
    employeeId= Faker().random_int(min=1000, max=9999)  # Generate a random employee ID
    name=Faker().name()  # Generate a random name
    emailId=Faker().email()  # Generate a random email  
    contactNumber=Faker().phone_number()  # Generate a random phone number
    designation=Faker().job()  # Generate a random job title
    dob_input=Faker().date_of_birth(minimum_age=18, maximum_age=65).strftime("%d-%m-%Y")  # Generate a random date of birth
    dob= datetime.strptime(dob_input, "%d-%m-%Y")  # Convert string to datetime object
    print(f"Index{index}")
    print(f"Employee Id: {employeeId}, Name: {name}, Email: {emailId}, Contact: {contactNumber}, Designation: {designation}, Dob: {dob.strftime('%d-%m-%Y')}")
