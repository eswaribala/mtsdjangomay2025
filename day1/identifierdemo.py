#read employee data
"""
Author: Parameswari
Date: 2023-10-01
Description: This script reads employee data from a user or it will generate date using faker.
"""

employeeId=input("Enter employee id: ")
name=input("Enter employee name: ")
emailId=input("Enter employee email: ")
contactNumber=input("Enter employee contact number: ")
designation=input("Enter employee designation: ")
#formatting the output
print("Employee Id: ", employeeId)
print("Employee Name: ", name)
print("Employee Email: ", emailId)      
print("Employee Contact Number: ", contactNumber)
print("Employee Designation: ", designation)
#displaying the output
print("Employee Details:")
print(f"Id: {employeeId}, Name: {name}, Email: {emailId}, Contact: {contactNumber}, Designation: {designation}")
print("EmployeeId=%s, Name=%s, Email=%s, Contact=%s, Designation=%s" % (employeeId, name, emailId, contactNumber, designation))