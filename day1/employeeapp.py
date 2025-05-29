from models.employee import Employee  
#create objects of Employee class

employee=Employee(1, "John Doe", "Software Engineer", 60000,"param@gmail.com",9952032862)
employee.set_id(4677)
print(employee.get_details())