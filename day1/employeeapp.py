from models.fulltimeemployee import FullTimeEmployee
#create objects of Employee class

employee=FullTimeEmployee(1, "John Doe", "Software Engineer", 60000,"param@gmail.com",9952032862, 5000.0)
employee.set_id(4677)
print(employee.get_name())
