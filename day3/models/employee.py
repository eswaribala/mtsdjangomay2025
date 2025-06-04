class Employee:
   
    #constructor overloading
    def __init__(self, *args):
        
        self.__first_name, self.__last_name, self.__salary, self.__email, self.__phone_number,self.__job_title,self.__hire_date,self.__status, self.__gender  = args
    
    def get_first_name(self):
        return self.__first_name
    def get_last_name(self):
        return self.__last_name
    def get_salary(self):
        return self.__salary    
    def get_email(self):
        return self.__email
    def get_phone_number(self):
        return self.__phone_number
    def get_job_title(self):
        return self.__job_title
    def get_hire_date(self):
        return self.__hire_date
    def get_status(self):
        return self.__status
    def get_gender(self):
        return self.__gender
    def set_first_name(self, first_name):   
        self.__first_name = first_name
    def set_last_name(self, last_name):
        self.__last_name = last_name
    def set_salary(self, salary):
        self.__salary = salary  
    def set_email(self, email):
        self.__email = email    
    def set_phone_number(self, phone_number):
        self.__phone_number = phone_number
    def set_job_title(self, job_title):
        self.__job_title = job_title
    def set_hire_date(self, hire_date):        
        self.__hire_date = hire_date
    def set_status(self, status):
        self.__status = status
    def set_gender(self,gender):
        self.__gender=gender


    
    