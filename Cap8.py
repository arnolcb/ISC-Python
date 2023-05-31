"""Notes from Chapter 8"""

# 8.1 - Lists   
#List can be empty

#Defining a list
list1 = [1,2,3,4,5]

#Accessing a list
print(list1[0]) #prints 1

print("For")
for i in list1:
    print(i)

#Changing a list
list1[0] = 10
print(list1[0]) #prints 10

#Adding to a list
list1.append(6)
#Append agrega un elemento a la lista

#Deleting from a list
del list1[0]
#del elimina un elemento de la lista

#Len of a list
print(len(list1)) #prints 5 porque se elimino el elemento 0

# 8.2 - Manipulating lists
#Concatenating lists

#List can be sliced using
t = [9,41,12,3,74,15]
print(t[1:3]) #prints [41,12]
