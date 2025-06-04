from exceptions.negativenumberexception import NegativeNumberException
from abc import ABC, abstractmethod
class Employee(ABC):
    #static variable
    employeeCount = 0
    #constructor overloading
    def __init__(self, *args):
        if len(args) == 1:
            self.__name = args[0]
        elif len(args) == 2:
            self.__id, self.__name = args[0], args[1]
        elif len(args) == 6:
            if(args[0] < 0 or args[3] < 0):
                raise NegativeNumberException(args[0], "Id and Salary cannot be negative.")
            else:
              self.__id, self.__name, self.__designation, self.__salary, self.__email, self.__contactNo = args
        
        else:
            self.__id, self.__name, self.__designation, self.__salary, self.__email, self.__contactNo = None
    """
    def __init__(self, id, name, designation, salary,email, contactNo):
        self.__id= id
        self.__name = name
        self.__designation = designation
        self.__salary = salary
        self.__email = email
        self.__contactNo = contactNo
    #def __init__(self,name):
        #self.__name = name
    """
    @property   #can be accessed like an attribute 
    def email(self):
        return self.__email
    def get_contact_no(self):
        return self.__contactNo
    @email.setter #can be set like an attribute
    def email(self, email):
        self.__email = email    
    def set_contact_no(self, contactNo):    
        self.__contactNo = contactNo
    def set_name(self, name):
        self.__name = name
    def set_designation(self, designation):
        self.__designation = designation     
    def set_salary(self, salary):
        self.__salary = salary      
    def set_id(self, id):
        self.__id = id  
    def get_id(self):   
        return self.__id
    def get_name(self): 
        return self.__name
    def get_designation(self):
        return self.__designation
    def get_salary(self):
        return self.__salary
    
    def get_details(self):  
        return f"Id:{self.__id},Name: {self.__name}, Designation: {self.__designation}, Salary: {self.__salary}"
    @abstractmethod
    def calculate_salary(self):
        pass  # This method should be implemented by subclasses
