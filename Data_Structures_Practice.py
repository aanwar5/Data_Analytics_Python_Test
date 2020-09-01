#!/usr/bin/env python
# coding: utf-8

# In[51]:


#Data Structures 
Names = ["Apple", "Banana", "Grape", "Pomegranate", "Lemon", "herb"]
print("Items in a tuple", Names)

A = Names[2]
print("Belonging to the Grapes family is ------->", A)

B = Names[1:3]
print("First three Numbers in the list ------>", B)

C = Names[0:]
print("I honestly don't know what this will print ------>", C)




#Further slightly advanced methods.
fam = [1.73, 1.68, 1.71, 1.89]
print("First List --->", fam)

fam1 = ["Hina", 0.73, "Ayesha", 1.68, "Sara", 1.77, "Kiran", 1.95]
print("The CC Family ---->", fam1)

#The following code shall print values starting from 1 i.e 0.73 and end it before 3.
print("Range of Values within the Anwar Family ---->" ,fam1[1:3])

#Lists within Lists
fam2=[["Hina", 0.73], ["Ayesha", 1.68], ["Sara", 1.77], ["Kiran", 1.95]]
print("Elements within the list fam2---->", fam2)
print("Second List(Classed as element) within list of fam2--->", fam2[2])
print(" ")
print("Print second item within second list of fam2 --->", fam2[2][0])

x = fam2[2][0]
all(type(d) == int for d in x) #checks whether the list value is an int or not. If it is an int it will print true, else false.

#changing values within strings 

fam1[1] = 0.80 #changes number to the right of Hina
print("New updated version of fam1 --> ", fam1)

#deletion of an element within a list. 
del(fam1[2])
print("New and updated-->", fam1) #The name Ayesha got deleted from the list.

#expansion of a list 
Updated = fam1 + ["Abdullah", 23]
print(Updated)

#inserting item at a specific point within a list.
fam1.insert(2,5000) #placed at position 2. All positons start from 0.Comes after 0.8
print("Adding item in fam1 -->", fam1)

#Append method; adds an element at the end of a list.
fam1.append("Talha") #adds Talha to the very end of the list of fam1
print("Addition of 5 in the family whatupp --->", fam1)

#inserting an item from one list to another list at the very end.
list_123 = [1,2,3,4,5]
fam1.extend(list_123)
print("New and updated -->", fam1)


#Dictionary Python Structures are mutable -->
#NO TWO KEYS MUST HAVE THE SAME VALUES according to the dictionary. 
#elements within the dictionary are immutable --> can't be updated.
#Items in dictionaries cannot be used to access using any index. Different from tuple and list.
#NOT INDEX BASED, it is key based.



#Floating Data Dictionaries
#printing the entire dictionary is easy
world = {"Afghanistan": 30.55, "Australia": 2.77, "Algeria": 39.21}
print("Values of the world-->", world)

#printing the value of a specific item within a dictionary
print("Accessing the 2nd element within a dictionary")
print("-->", world["Australia"]) #This shall print out 2.77 


#Assigning to a key value which does not exist
world["Pakistan"] = 1947
print("New item has been added to the Dictionary -->", world)

#changing the elements within the dictionary
world["Algeria"] = 2000
print(world)

#deleting items within the dictionary 
del(world["Pakistan"])
print(world)






