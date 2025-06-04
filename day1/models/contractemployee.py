from models.employee import Employee
class ContractEmployee(Employee):
    def __init__(self, id, name, designation, salary,email, contactNo,hourly_rate, hours_worked):
        super().__init__(id, name, designation, salary,email, contactNo)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_pay(self):
        return self.hourly_rate * self.hours_worked

    def __str__(self):
        return f"ContractEmployee(name={self.name}, hourly_rate={self.hourly_rate}, hours_worked={self.hours_worked})"
    
    def get_details(self):  
        return f"Id:{self.__id},Name: {self.__name}, Designation: {self.__designation}, Salary: {self.__salary}, Bonus: {self.__bonus}"
  
    def calculate_salary(self):
        Employee.employeeCount += 1
        return self.hourly_rate * self.hours_worked