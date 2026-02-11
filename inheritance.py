#inheratnce a child class inherints attributes  and method from parent
#super/parent class
class Animal:

    def __init__(self,name,age):
        self.name=name
        self.age=age
    def speak(self):
        return f'hello'
    def supermethod(self):
        return f'hello form a  method in super class'
#child/sub class
class Dog(Animal):
    def speak(self):
        return 'bark bark'
    def chrome(self):
        return f' hello from  a method in dog class'
#add a class cat that inherits from animal
#add speak method-meow

#create a dog object
mydog=Dog("bob",9)
print(mydog.name)
#call a parent method
print(mydog.supermethod())
#overidding method
print(mydog.speak())
#calling our own method
print(mydog.chrome())
#create a  cat object
#call the speak method
#call me the supermethod()
