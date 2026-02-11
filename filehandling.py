

#open(filename,mode)
#modes-r-read,w-write,a-append,x-create
#write
x=open("demo.txt",'w')
x.write("This is python file handling")
x.close()
#append
y=open("demo.txt",'a')
y.write('\nThis is some appended text')
y.close()
#read
z=open('demo.txt','r')
print(z.read())
z.close()
#x-create
file=open("example.txt",'x')
file.write("hello python")
file.write("this is python")
file.close()
