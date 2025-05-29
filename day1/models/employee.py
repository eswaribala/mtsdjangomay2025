class Employee:
    def __init__(self, id, name, designation, salary,email, contactNo):
        self.id= id
        self.name = name
        self.designation = designation
        self.salary = salary
        self.email = email
        self.contactNo = contactNo

    def get_details(self):
        return f"Name: {self.name}, Designation: {self.designation}, Salary: {self.salary}"

    