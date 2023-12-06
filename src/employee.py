"""
Employee module
"""


class Employee:
    """
    class Employee
    """
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    def print_initials(self):
        """
        prints initials
        """
        print(f'Name: {self.name}, surname: {self.surname}, age: {self.age} ')

    @staticmethod
    def say_hello():
        """
        employee says hello
        """
        print("Hello")


class Programmer(Employee):
    """
    implementation of Programmer class
    """

    def count_salary(self):
        """
        counts salary
        """
        return 14000 * 5


class Manager(Employee):
    """
    Implementation of manager
    """
    def count_salary(self):
        return 14000 * 2


def print_employee_type(empl_obj):
    print(f'Current employee belongs to Employee  type? {isinstance(empl_obj, Employee)}')
    print(f'Employee {empl_obj.name} is of {type(empl_obj)} type ')
    print(f"Employees'  salary is {empl_obj.count_salary}")

class BackendEngineer(Programmer):
    """
    Implementation of backend Engineer
    """

class FrontendEngineer(Programmer):
    """
    Implementation of frontend engineer
    """

class CEOManager(Manager):
    """
    Implementation of CEO Manager
    """

class HRManager(Manager):
    """
    Implementation of HR Manager
    """


employee_1 = Programmer( name='FirstName', surname='FirstSurname', age=28)
employee_2 = Manager( name='SecondName', surname='SecondSurname', age=65)
employee_3 = CEOManager( name='SecondName', surname='SecondSurname', age=65)

employee_4 = HRManager( name='SecondName', surname='SecondSurname', age=65)
employee_5 = BackendEngineer( name='FirstName', surname='FirstSurname', age=28)
employee_6 = FrontendEngineer( name='FirstName', surname='FirstSurname', age=28)
#employee_1.print_initials()
#print(employee_1.count_salary())
#employee_2.print_initials()
#print(employee_2.count_salary())


employees = [employee_1, employee_2, employee_3, employee_4, employee_5, employee_6]
for empl in employees:
    if isinstance(empl, Programmer) or isinstance(empl, HRManager):
        print(print_employee_type(empl))
