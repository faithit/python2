#functions-perform a specific task
"""
def functionname():
    block of code

"""
def demo():
    print("hello goodafternon")
#calling the function
demo()
demo()

# function with parameter
def greetings(name):
    print("hello",name)
#calling the function
greetings("jane")
greetings("otieno")

#a function with multiple parameters
def studentInfo(first_name,age=18):
    print(f"hello {first_name} you are {age} years old")
#calling the function
studentInfo("david",17)
studentInfo("mary",21)
studentInfo("cate")
#function that calculates area of rectangle l*w
def areaOfRectangle(l,w):
    area=l*w
    print(f"The area of rectangle with length {l} and width {w} is {area}")
#calling the function
areaOfRectangle(70,56)
areaOfRectangle(10,20)
#a function that calculates area of a circle .a=3.14*r*r
def areaOfCircle(r):
    area=3.14*r*r
    print(f"The area of circle with radius {r} is {area}")

areaOfCircle(7)
