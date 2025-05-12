"""
Create a class Department and a class Employee. Use aggregation by having a Department object store a reference to an Employee object that exists independently of it.
"""



class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def display_employee(self):
        print(f"Employee: {self.name}, Position: {self.position}")

class Department:
    def __init__(self, department_name, employee):
        self.department_name = department_name
        self.employee = employee

    def display_department(self):
        print(f"Department: {self.department_name}")
        self.employee.display_employee()

employee = Employee("John Doe", "Software Engineer")

department = Department("IT", employee)

department.display_department()
