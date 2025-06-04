from models.employee import Employee
class FullTimeEmployee(Employee):
    def __init__(self, id, name, designation, salary,email, contactNo,bonus: float):
        super().__init__(id, name, designation, salary,email, contactNo)
        self.__bonus = bonus

    def get_details(self):  
        return f"Id:{self.__id},Name: {self.__name}, Designation: {self.__designation}, Salary: {self.__salary}, Bonus: {self.__bonus}"
  
    def calculate_salary(self):
        Employee.employeeCount += 1
        return self.get_salary() + self.get_salary()* 0.10 - self.get_salary() * 0.12 
    