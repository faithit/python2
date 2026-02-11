
#function with return keyword return a value
#function thats add two numbers
def addTwoNumbers(a,b):
    sum=a+b
    return sum
#calling the function and storing the returned valuie in a variable
result=addTwoNumbers(30,50)
print("The sum is",result)
#way two
print(addTwoNumbers(60,59))
#function that multiplies 3 numbers
def multiply(x,y,z):
    return x*y*z
#calling the function
print(multiply(10,50,40))
#function that checks if a number is even or odd
def evenOrOdd(c):
    if c%2==0:
        print(c,"is an even number")
    else:
        print(c,"is an odd number")
#get user input
num=int(input("enter a number to check if even or odd"))
#calling the function
evenOrOdd(num)
#function that finds maximum of two numbers
def maximum(x,y):
    return max(x,y)
print(maximum(45,78))



