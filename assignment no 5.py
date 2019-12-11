#!/usr/bin/env python
# coding: utf-8

# 
# # Assignment # 5

# ##                                                            task#1

# In[ ]:


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
n=int(input("Enter a positive number to compute the factiorial : "))
print(factorial(n))


# ##                                                            task#2

# In[9]:


def string_test(s):
    d={"UPPER_CASE":0, "LOWER_CASE":0}
    for c in s:
        if c.isupper():
           d["UPPER_CASE"]+=1
        elif c.islower():
           d["LOWER_CASE"]+=1
        else:
           pass
    print ("Original String : ", s)
    print ("No. of Upper case characters : ", d["UPPER_CASE"])
    print ("No. of Lower case Characters : ", d["LOWER_CASE"])
a =input ("write a paragraph")
string_test(a)


# ##                                                          task#3

# In[10]:


list1 = [1, 21, 45, 56, 76, 73] 
  

for num in list1: 
      
 
    if num % 2 == 0: 
       print(num, end = " ") 


# ##                                                         task#4

# In[31]:


x = "madam"
w = "" 
for i in x: 
    w = i + w 
    if (x==w): 
        print("YES") 
        


# ##                                                       task#5

# In[34]:



num = int(input("enter number"))
  
 
if num > 1: 
        
   for i in range(2, num//2): 
         
       if (num % i) == 0: 
           print(num, "is not a prime number") 
           break
   else: 
       print(num, "is a prime number") 
  
else: 
   print(num, "is not a prime number") 


# ##                                                             task # 6

# In[42]:


def a(*names):
  

   
   for name in names:
    print("things you buy during shooping is",name)

a("cake","clothes ","house holds","food")


# In[ ]:





# In[ ]:




