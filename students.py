#CLASS IA A BLUEPRINT FOR CREATING OBJECTS
#object-is an uinsance of a class
class Student:
    #constructor
    #runs automallically when an object is created
    def __init__(self,name,age,course):
        self.name=name
        self.age=age
        self.course=course

    def __str__(self):
        return f"The student name : {self.name}  age : {self.age} :course  is {self.course}"
    def get_email(self):
        return f'{self.name}@emobilis.ac.ke'

#create an object
#object is an instance of a class
#objectname=classname(values)
student1=Student("jane",17,"MIT")
student2=Student("kamau",18,"Cybersecurity")
print(student1)
print(student2)
#call our function
print(student1.get_email())
print(student2.get_email())

