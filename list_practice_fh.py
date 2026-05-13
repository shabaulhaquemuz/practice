#!/usr/bin/env python
# coding: utf-8

# In[12]:


#1.Write a Python program to find the maximum element in a list of numbers without max functions
#numbers = [10, 20, 4, 45, 99]
#The maximum element is: 99
x=[10,20,4,45,99]
maxx=x[0]
for i in range(len(x)):
    if(x[i]>maxx):
        maxx=x[i]
print(maxx)


# In[13]:


#2.Write a Python program to sum all the elements in a list of numbers.
#a. numbers = [10, 20, 30, 40]
#b. The sum of all elements is: 100
x2=[10,20,30,40]
summ=0
for i in x2:
    summ+=i
print(summ)


# In[14]:


#3.Write a Python program to reverse a list without reverse or slicing operator
#a. numbers = [1, 2, 3, 4, 5]
#b. Reversed list: [5, 4, 3, 2, 1]
x3=[1,2,3,4,5]
reverse=[]
for i in range(len(x3)):
    x=x3.pop()
    reverse.append(x)
print(reverse)


# In[15]:


#4.Write a Python program to sort a list in ascending order without sort functions
x4=[4,76,54,67,90,1000,800,900]
for i in range(len(x4)):
    for j in range(i+1,len(x4)):
        if(x4[i]>x4[j]):
            x4[i],x4[j]=x4[j],x4[i]
print(x4)


# In[16]:


#4.Write a Python program to sort a list in ascending order without sort functions
x4=[4,76,54,67,90,1000,800,900]
for i in range(len(x4)):
    for j in range(i+1,len(x4)):
        if(x4[i]<x4[j]):
            x4[i],x4[j]=x4[j],x4[i]
print(x4)


# In[ ]:





# In[17]:


#5.Write a Python program to remove duplicates from a list while maintaining the order of elements.
#a. numbers = [1, 2, 2, 3, 4, 4, 5]
#b. List after removing duplicates: [1, 2, 3, 4, 5]
x5=[1, 2, 2, 3, 4, 4, 5]
new=[]
for i in x5:
    if(i not in new):
        new.append(i)
print(new)


# In[ ]:





# In[26]:


#6.Write a Python program to find all pairs of numbers in a list that add up to a specific target sum.
#a. numbers = [1, 2, 3, 4, 3, 5, 6] target_sum = 6
#b. Pairs that add up to 6: [(3, 3), (2, 4), (1, 5)]
x6=[1, 2, 3, 4, 3, 5, 6]
new=[]
for i in range(len(x6)):
    for j in range(i+1,len(x6)):
        if(x6[i]+x6[j]==6):
            new.append((x6[i],x6[j]))
print(new)
new.sort(reverse=True)
print(new)


# In[28]:


#7.Write a Python program to flatten a nested list (list within lists) into a single list.
#a. nested_list = [1, [2, 3], [4, [5, 6], 7], 8]
#b. Flattened list: [1, 2, 3, 4, 5, 6, 7, 8]
nested_list = [1, [2, 3], [4, [5, 6], 7], 8]
new=[]
flattened=[]
for i in nested_list:
    if(type(i)!=list):
        new.append(i)
    else:
        new.extend(i)
print(new)
for j in new:
    if(type(j)!=list):
        flattened.append(j)
    else:
        flattened.extend(j)
print(flattened)


# In[32]:


#8.Write a Python program to find the sum of the elements in a list, excluding the largest and smallest element. Don’t use max or min functions
#a. numbers = [1, 2, 3, 4, 5]
#b. Sum excluding the largest and smallest element: 9
numbers = [1, 2, 3, 4, 5,5]
maxx=numbers[0]
minn=numbers[0]
summ=0
for i in range(len(numbers)):
    if(numbers[i]>maxx):
        maxx=numbers[i]
    elif(numbers[i]<minn):
        minn=numbers[i]
print(maxx,minn)
for j in range(len(numbers)):
    if(numbers[j]!=maxx and numbers[j]!=minn):
        summ+=numbers[j]
print(summ)




# In[36]:


#Write a Python program to check if a list is a palindrome (reads the same backward as forward) using two pointer approach
#a. numbers = [1, 2, 3, 2, 1]
#b. True
numbers = [1, 2, 3, 2, 1,1]
start=0
end=len(numbers)-1
count=0
for i in range(len(numbers)//2):
    if(numbers[start]!=numbers[end]):
        count=1
        break
    start+=1
    end-=1
if(count==0):
    print("Palindrome")
else:
    print("Not Palindrome")



# In[37]:


#10. Write a function to remove duplicate elements from a list.
#a. numbers = [1, 2, 3, 2, 4, 5, 1, 6]
#b. [1, 2, 3, 4, 5, 6]
numbers = [1, 2, 3, 2, 4, 5, 1, 6]
unique=[]
for i in numbers:
    if(i not in unique):
        unique.append(i)
print(unique)


# In[38]:


#10. Write a function to remove duplicate elements from a list.
#a. numbers = [1, 2, 3, 2, 4, 5, 1, 6]
#b. [1, 2, 3, 4, 5, 6]
def unique_list(mylist):
    unique=[]
    for i in mylist:
        if(i not in unique):
            unique.append(i)
    print(unique)
unique_list([1, 2, 3, 2, 4, 5, 1, 6])



# In[44]:


#11. Find Common Elements in Two Lists
#a. list1 = [1, 2, 3, 4, 5]
#b. list2 = [3, 4, 5, 6, 7]
#c. Result: [3, 4, 5]
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
result=[]
for i in list1:
    for j in list2:
        if(i==j and i not in result):
            result.append(i)
print(result)


# In[52]:


#12. Find the Longest Word in a List
#a. words = ["apple", "banana", "strawberry", "kiwi"]
#b. Strawberry
words = ["apple", "banana", "strawberry", "kiwi","jhdwgegddewhdgwj"]
longest=words[0]
for i in words:
    if(len(i)>len(longest)):
        longest=i
print(longest)


# In[56]:


#14. Find Missing Number in a List
#You are given a list of n-1 numbers in the range 1 to n. One number is missing from the sequence. Find the missing number.
#a. numbers = [1, 2, 4, 5, 6]
#b. 3
numbers = [1, 2, 4, 5, 6]
start=0
nexxt=1
for i in range(len(numbers)-1):
    if((numbers[nexxt]-numbers[start])!=1):
        print(numbers[nexxt]-1)
    start+=1
    nexxt+=1  


# In[62]:


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
        print("1st non-repeating element is:",numbers[i])
        break


# In[65]:


#16. Move All Zeros to the End
#Given a list of integers, move all zeros to the end while maintaining the relative order of non-zero elements. Don’t use any inbuilt functions
#a. numbers = [0, 1, 0, 3, 12]
#b. [1, 3, 12, 0, 0]
numbers = [0, 1, 0, 3, 12]
new=[]
for i in numbers:
    if(i!=0):
        new.append(i)
for j in numbers:
    if(j==0):
        new.append(j)
print(new)


# In[67]:


#17. Find Elements Greater Than Their Left Neighbor
#a. numbers = [1, 3, 2, 6, 5, 8, 7]
#b. [3, 6, 8]
numbers = [1, 3, 2, 6, 5, 8, 7]
start=0
nexxt=1
for i in range(len(numbers)-1):
    if(numbers[nexxt]>numbers[start]):
        print(numbers[nexxt])
    start+=1
    nexxt+=1



# In[73]:


#18. Find Triplets That Sum to Zero
#Given a list of numbers, find all unique triplets (a, b, c) such that a + b + c = 0.
#a. numbers = [-1, 0, 1, 2, -1, -4]
#b. Expected Output: [(-1, -1, 2), (-1, 0, 1)]
numbers = [-1, 0, 1, 2, -1, -4]
mylist=[]
for i in range(len(numbers)):
    for j in range(i+1,len(numbers)):
        for k in range(j+1,len(numbers)):
            if((numbers[i]+numbers[j]+numbers[k])==0):
                triplets=[numbers[i],numbers[j],numbers[k]]
                triplets.sort()
                if(triplets not in mylist):
                    mylist.append(triplets)
print(mylist)




# In[76]:


#Finding second maximum in a list
mylist=[5764,23,43,67,865,42,10000]
if(mylist[0]>mylist[1]):
    maximum=mylist[0]
    second_maximum=mylist[1]
else:
    maximum=mylist[1]
    second_maximum=mylist[0]
for i in range(2,len(mylist)):
    if(mylist[i]>maximum):
        second_maximum=maximum
        maximum=mylist[i]
    elif(mylist[i]>second_maximum and mylist[i]!=maximum):
        second_maximum=mylist[i]
print(maximum,second_maximum)



# In[ ]:




