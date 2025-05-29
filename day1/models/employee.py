class Employee:
    def __init__(self, id, name, designation, salary,email, contactNo):
        self.__id= id
        self.__name = name
        self.__designation = designation
        self.__salary = salary
        self.__email = email
        self.__contactNo = contactNo

    def get_details(self):
        return f"Id:{self.__id},Name: {self.__name}, Designation: {self.__designation}, Salary: {self.__salary}"

    