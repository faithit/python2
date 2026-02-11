#write
with open('chrome.txt',"w") as  x:
    x.write("hi,this a some text")
#read
with open('chrome.txt','r') as file:
    content=file.read()
    print(content)