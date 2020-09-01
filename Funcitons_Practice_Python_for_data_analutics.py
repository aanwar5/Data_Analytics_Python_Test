#!/usr/bin/env python
# coding: utf-8

# In[1]:


#defining a function i.e Main or test.

def Test123():
    for i in range(10): 
       print("Repeat after me")
    return

Test123()

def changeme(mylist):
    mylist =[1,2,3,4]
    print("values inside function", mylist)
    return

#even tho the name is the same, as it is outside of the function,it will still be regarded as something seperate
mylist = [10,20,30,40]
changeme(mylist)
print("Balues outside the function", mylist)


# In[2]:


#difference between the My list function when you return mylist properly 
def changeme(mylist):
    mylist =[1,2,3,4]
    print("values inside function", mylist)
    return mylist  #notice how I've added return mylist here

#even tho the name is the same, as it is outside of the function,it will still be regarded as something seperate
mylist = [10,20,30,40]
mylist1 = changeme(mylist)
print("Balues outside the function", mylist1) 

#values which shall be printed shall be the same.

def fact(n):
    """To find factorial value"""
    prod=1
    while n>=1:
        prod *=n
        n-=1
    return prod

#display factorial 
for i in range(1, 11):
    print("factorial of", i, "is", fact(i))


# In[10]:


#function inside another function
def display(str):
    def message():
        return "How are you ? "
    result=message() + str
    return result 

print(display("Abdullah"))

print(display)
a = input("Put in your response here->")
print(a)


# In[11]:


def modify(x):
    "reassign a value to the variable"
    x = 15
    print(x, id(x))
    
x = 10
modify(x)
print(x, id(x))


# In[14]:


#making a function hello
def hello(Greet):
    greet_1 = input("Insert your name: ")
    return Greet + greet_1
def lollipop():
    return 'How are you ? '
print(hello(lollipop()))


# In[ ]:





# In[ ]:




