"""
try:
    block ofr code that can cause error
except:
    #code thats runs if error happens
"""
try:
    num=int(input("enter a number"))
    print(10/num)
except:
    print("you cannot divide a number by zero")
#another example
try:
    print(x)
except NameError:
    print("The variable is not defined")
#another example
try:
    with open('abcd.txt','r') as x:
        print(x.read())
except FileNotFoundError:
    print("file not found")