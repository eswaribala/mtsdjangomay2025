#read employee data
"""
Author: Parameswari
Date: 2023-10-01
Description: This script reads employee data from a user or it will generate date using faker.
"""
from datetime import datetime
#type casting
employeeId=int(input("Enter employee id: "))
name=input("Enter employee name: ")
emailId=input("Enter employee email: ")
contactNumber=input("Enter employee contact number: ")
designation=input("Enter employee designation: ")
dob_input=input("Enter employee date of birth (dd-mm-yyyy): ")
dob= datetime.strptime(dob_input, "%d-%m-%Y")  # Convert string to datetime object

#type checking
print(type(employeeId))
print(type(name))   
print(type(emailId))
print(type(contactNumber))          
print(type(designation))
print(type(dob))    

#employeeNo=int(employeeId)  # Convert employeeId to integer
#print(type(employeeNo))

#formatting the output
print("Employee Id: ", employeeId)
print("Employee Name: ", name)
print("Employee Email: ", emailId)      
print("Employee Contact Number: ", contactNumber)
print("Employee Designation: ", designation)
print("Employee Date of Birth: ", dob.strftime("%d-%m-%Y"))
#displaying the output
print("Employee Details:")
print(f"Id: {employeeId}, Name: {name}, Email: {emailId}, Contact: {contactNumber}, Designation: {designation}, Dob: {dob.strftime('%d-%m-%Y')}")
print("EmployeeId=%s, Name=%s, Email=%s, Contact=%s, Designation=%s,Dob=%s" % (employeeId, name, emailId, contactNumber, designation, dob.strftime('%d-%m-%Y')))