

#list=used to multiple elements in a single variable
#list  is ordered,changeable and allows duplicates
students=["johari","mary","keter","jane","allison"]
mynums=[78,99,67,45,90,75]
print(students)
print(mynums)
print(type(students))
print(type(mynums))
#len()-length
print(len(students))
print(len(mynums))
#acessing list item
print(students[0])
print(students[3])
#modifying list item
print(students)
students[1]="Angela"
print(students)
#list methods,append(),remove(),pop(),
#append-adds an item at the end
students.append("john")
print(students)
#remove() -removes a specific item
students.remove("jane")
print(students)
#insert()-adds an element at spefic index
students.insert(1,"lewis")
print(students)
#looping through a list
for x in students:
    print(x)




