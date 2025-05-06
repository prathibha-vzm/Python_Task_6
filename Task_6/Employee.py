#Question 2

#Base class
class Employee:
    #construcctor with 2 arguments
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

    #Method to calculate salary
    def calculate_salary(self):
        #calculating the PF amount
        pf = (12/100)*self.salary

        #calculating the salary
        self.salary-=pf

        #printing
        print(f"Temporary_Employee_Name: {self.name}-Salary:{self.salary}")

#Subcalss with parent
class RegularEmployee(Employee):
    # constructor with 2 arguments
    def __init__(self,name,salary):
        super().__init__(name,salary)
        self.name=name
        self.salary=salary

    #Method Overriding(Run-time Polymorphism)
    def calculate_salary(self):
        # calculating the PF amount and TAX
        pf = (12/100)*self.salary
        tax=(5/100)*self.salary

        # calculating the salary
        self.salary=self.salary-pf-tax

        # printing the answer
        print(f"Regular_Employee_Name: {self.name}-Salary:{self.salary}")

#Subclass with parent
class ContractEmployee(Employee):
    def __init__(self,name,salary):
        super().__init__(name, salary)
        self.name=name
        self.salary=salary

    # Method Overriding(Run-time Polymorphism)
    def calculate_salary(self):

        # calculating the TAX and Adding benefits
        tax_deduction=(20/100)*self.salary
        additional_benefits=1000

        # calculating the salary
        self.salary=self.salary-tax_deduction+additional_benefits

        # printing the answer
        print(f"Contractor_Name: {self.name}-Salary:{self.salary}")

#Subclass with parent
class Manager(Employee):
    def __init__(self,name,salary):
        super().__init__(name, salary)
        self.name=name
        self.salary=salary

    # Method Overriding(Run-time Polymorphism)
    def calculate_salary(self):

        # calculating the House Rent and PF
        hrs=(40/100)*self.salary
        pf = (12/100)*self.salary

        # calculating the salary
        self.salary=self.salary-pf+hrs

        # printing the answer
        print(f"Manager_Name: {self.name}-Salary:{self.salary}")

#Creating an object for each class and input the values
Employee_object=Employee("Danya",30000)
RegularEmployee_object=RegularEmployee("Prabha",50000)
ContractEmployee_object=ContractEmployee("Vino",55000)
Manager_object=Manager("Bhavani",400000)

#Using For loop to call the method calculate_salary
for employee in (Employee_object,RegularEmployee_object,ContractEmployee_object,Manager_object):
    employee.calculate_salary()
