#class-is a blueprint for creatings objects
#object is an instance of a class
#objects-attributes and methods
class Employee:
    def __init__(self,first_name,last_name,department,salary):
        self.first_name=first_name
        self.last_name=last_name
        self.department=department
        self.salary=salary
    #returns a readable string when you print objetc
    def __str__(self):
        return f'{self.first_name} {self.last_name} department :{self.department} {self.salary}'
    #returns annual salary
    def annual_salary(self):
        return f'{self.salary *12}'
    #returns fullname
    def fullname(self):
        return f'{self.first_name} {self.last_name}'

#create an  object
emp1=Employee('mark',"kamau","IT",50000)
#another object
emp2=Employee('JACOB','james','Marketing',20000)
#Access the attribute value
print(emp1.first_name)
print(emp1.department)
print(emp2.first_name)
#printing object1
print(emp1)
#calling the annual_salary()
print(emp1.annual_salary())
print(f'{emp1.first_name} salary is {emp1.annual_salary()}')
#printing object2
print(emp2)
#calling the annual_salary()
print(emp2.annual_salary())
print(f'{emp2.first_name} salary is {emp2.annual_salary()}')
#CALLING THE FULLNAME()
print(emp1.fullname())
print(emp2.fullname())
