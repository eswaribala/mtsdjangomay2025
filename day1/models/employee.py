class Employee:
    def __init__(self, id, name, designation, salary,email, contactNo):
        self.__id= id
        self.__name = name
        self.__designation = designation
        self.__salary = salary
        self.__email = email
        self.__contactNo = contactNo
    #def __init__(self,name):
        #self.__name = name
        
    def get_email(self):
        return self.__email
    def get_contact_no(self):
        return self.__contactNo
    def set_email(self, email):
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

    