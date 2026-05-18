#!/usr/bin/env python
# coding: utf-8

# In[28]:


mylist=[123,45,678,999,99,9876,543]
if(mylist[0]>mylist[1]):
    maximum=mylist[0]
    second_maximum=mylist[1]
elif(mylist[1]>mylist[0]):
    maximum=mylist[1]
    second_maximum=mylist[0]
for i in range(2,len(mylist)):
    if(mylist[i]>maximum):
        second_maximum=maximum
        maximum=mylist[i]
    elif(mylist[i]>second_maximum and mylist[i]!=maximum):
        second_maximum=mylist[i]
print(maximum,second_maximum)


# In[31]:


#15. Find the First Non-Repeating Element
#Given a list of integers, find the first element that appears only once.
#a. numbers = [4, 5, 1, 2, 0, 4, 5, 2]
#b. Expected Output: 1
numbers = [4, 5, 1, 2, 0, 4, 5, 2]
for i in range(len(numbers)):
    count=0
    for j in range(len(numbers)):
        if(numbers[i]==numbers[j] and i!=j):
            count+=1
            break
    if(count==0):
        print(numbers[i])
        break


# In[ ]:




