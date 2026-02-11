#module- python file that contains python code,it can have have functions,variablkes
# etc that you want to include ijn your file
#import themodule
import math as fm
import random
import datetime

print(fm.sqrt(25))
print(fm.pi)
print(fm.floor(3.46))
print(fm.ceil(3.46))
#generate  random int btwn 5-14
print(random.randint(5,14))
#gerenrate random num btwn o-1
print(random.random())
#generate current date and time
print(datetime.datetime.now())
x=datetime.datetime.now()
print(x.year)
print(x.month)
print(x.hour)
