#!/usr/bin/env python
# coding: utf-8

# In[2]:


#fetch value greater than 10 and store it in new_list
list1=[10,4,5,67,89,90,1,2,3,1000]
newlist=[]
for i in list1:
    if(i>10):
        newlist.append(i)
print(newlist)


# In[4]:


list1=[10,4,5,67,89,90,1,2,3,1000]
newlist=list(filter(lambda x:x>10,list1))
print(newlist)


# In[12]:


add=lambda a,b:a*b
add(4,5)


# In[13]:


subt=lambda a,b:a-b
subt(5,4)


# In[14]:


addi=lambda a,b:a+b
addi(4,5)


# In[15]:


#lambda with filter
list1=[1,2,3,4,5,6,7,8]
new=list(filter(lambda x:x>5,list1))
print(new)


# In[17]:


list2=[1,2,3,4,5,6,7,8,9,10]
new=list(filter(lambda x:x%2==0,list2))
print(new)


# In[18]:


#lambda with map
list3=[1,2,3,4,5,6,7,8]
new=list(map(lambda x:x**2,list3))
print(new)


# In[21]:


#list comprehension
list1=[10,4,5,67,89,90,1,2,3,1000]
new=[i for i in list1]
print(new)


# In[22]:


list1=[10,4,5,67,89,90,1,2,3,1000]
new=[i for i in list1 if(i%2==0)]
print(new)


# In[23]:


list3=[i for i in range(1,10)]
print(list3)


# In[25]:


#dictionary comprehension
d={i:i**2 for i in range(1,10)}
d


# In[26]:


#print squares(list)
list1=[i**2 for i in range(1,10)]
print(list1)


# In[27]:


#print squares(dict)
d={i:i**2 for i in range(1,5)}
print(d)


# In[28]:


#to print the elements of string data type from the list
mylist=[10,20,30,"hey","naina",10,"29"]
for i in mylist:
    if(type(i)==str):
        print(i)


# In[29]:


##to find the maximum in a list
mylist2=[10,1000,20,30,15,6,7,8,999]
maxx=mylist2[0]
for i in range(len(mylist2)):
    if(mylist2[i]>maxx):
        maxx=mylist2[i]
print(maxx)


# In[30]:


##average of elements of a list
mylist5=[10,20,30,15,6,7,8,999]
summ=0
count=0
for i in mylist5:
    summ+=i
    count+=1
average=summ/count
print(summ)
print(average)


# In[31]:


##to check which element of the list has more than 4 letters
mylist6=['hllo','hey','user','aman','shabaul','haque']
for i in mylist6:
    if(len(i)>4):
        print(i)


# In[32]:


#finding minimum(-ve values) using min=0,max cant be founded for -ve values from this method
V=[-1,-34,-2,-543,-56,-3212]
minn=V[0]
for i in range(len(V)):
    if(V[i]<minn):
        minn=V[i]
print(minn)


# In[37]:


o=[5764,23,43,67,865,42]
o.sort()
o


# In[38]:


o=[5764,23,43,67,865,42]
o.sort(reverse=True)
o


# In[39]:


o=[5764,23,43,67,865,42]
a=sorted(o)
a


# In[40]:


o=[5764,23,43,67,865,42]
a=sorted(o,reverse=True)
a


# In[42]:


#max
o=[5764,23,43,67,865,42]
o.sort(reverse=True)
o[0]


# In[43]:


#min
o=[5764,23,43,67,865,42]
o.sort()
o[0]



# In[44]:


#second max
o=[5764,23,43,67,865,42]
o.sort(reverse=True)
o[1]


# In[45]:


#second min
#second max
o=[5764,23,43,67,865,42]
o.sort()
o[1]



# In[46]:


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
print(maximum)
print(second_maximum)


# In[47]:


#finding duplicate in a list and create a new list for duplicate
p=[22,3,2,4,55,66,33,222,222,22,3,55]
new=[]
duplicate=[]
for i in p:
    if(i not in new):
        new.append(i)
    else:
        duplicate.append(i)
print(new)
print(duplicate)


# In[71]:


p=[22,3,2,4,55,66,33,222,222,22,3,55,222]
new=[]
print("duplicate elements are:")
for i in p:
    if(i not in new):
        new.append(i)
    else:
        print(i,end=" ")


# In[51]:


#nested loop
#nested loop
list10=[10,20,30,40]
for i in range(0,1):
    print(i,list10[i])


# In[52]:


list11=[10,20,30,40]
for i in range(0,3):
    print(i,list11[i])


# In[53]:


list12=[10,20,30,40]
for i in range(len(list12)):
    print(i,list12[i])


# In[54]:


list12=[10,20,30,40]
for i in range(len(list12)):
    print(i,list12)


# In[55]:


list13=[10,20,30,40]
for i in range(0,1):
    print(i)
    for j in range(1,3):
        print(i,list13[i],j,list13[j])


# In[56]:


list14=[10,20,30,40]
for i in range(0,2):
    print(list14[i])
    for j in range(1,4):
        print(i,list14[i],j,list14[j])


# In[57]:


list15=[10,20,30,40]
for i in range(0,4):
    print(list15[i])
    for j in range(1,4):
        print(i,list15[i],list15[j])


# In[78]:


#to check duplicate elements in the list
# Print unique duplicate elements using two for loops”
# “Identify duplicates in a list using nested loops (no repetition)
list15 = [10, 20, 30, 40, 10, 20,20,30,30]
duplicate=[]
for i in range(len(list15)):
    for j in range(i+1,len(list15)):
        if(list15[i]==list15[j] and list15[i] not in duplicate):
            duplicate.append(list15[i])
print(duplicate)


# In[62]:


#to check if sum of two elements of a list is 9
list18=[1,2,3,7,14,6,4,5]
for i in range(len(list18)):
    for j in range(i+1,len(list18)):
        if(list18[i]+list18[j]==9):
            print(list18[i],list18[j])


# In[68]:


#to print duplicate characters from a string
string="hey usereh" 
duplicate=[]
for i in range(len(string)):
    for j in range(i+1,len(string)):
        if(string[i]==string[j] and string[i] not in duplicate):
            duplicate.append(string[i])
print(duplicate)


# In[65]:


#to print duplicate characters from a string
string="hey usereh" 
new=[]
for i in range(len(string)):
    if(string[i] not in new):
        new.append(string[i])
    else:
        print(string[i])


# In[66]:


#to print duplicate characters from a string
string="hey usere" 
newlist=[]
duplicate=[]
for i in string:
    if(i not in newlist):
        newlist.append(i)
    else:
        duplicate.append(i)
print(newlist,duplicate)


# In[75]:


p=[22,3,2,4,55,66,33,222,222,22,3,55,222,222]
new=[]
duplicate=[]
for i in p:
    if(i not in new):
        new.append(i)
    else:
        if(i not in duplicate):
            print(i,end=" ")
            duplicate.append(i)


# In[81]:


#finding two elements sum of which is 9 using single loop and using two pointer approach(while loop)
list19 = [1,2,3,5,7,11,18,6,4]
print(list19)
list19.sort()
print(list19)
start=0
end=len(list19)-1
while(start<end):
    p=list19[start]+list19[end]
    if(p>9):
        end-=1
    elif(p<9):
        start+=1
    else:
        print(list19[start],list19[end])
        start+=1
        end-=1


# In[84]:


#scheck if a string is palindrome
string="sarasw"
start=0
end=len(string)-1
count=0
for i in range(len(string)//2):
    if(string[start]!=string[end]):
        count=1
        break
    start+=1
    end-=1
if(count==0):
    print("Palindrome")
else:
    print("Not a Palindrome")


# In[85]:


#3.Write a Python program to reverse a list without reverse or slicing operator
#a. numbers = [1, 2, 3, 4, 5]
#b. Reversed list: [5, 4, 3, 2, 1]
numbers = [1, 2, 3, 4, 5]
numbers[::-1]


# In[90]:


numbers = [1, 2, 3, 4, 5]
new=[]
for i in range(len(numbers)):
    x=numbers.pop()
    new.append(x)
print(new)



# In[96]:


#4.Write a Python program to sort a list in ascending order without sort functions
x4=[4,76,54,67,90,1000,800,900]
for i in range(len(x4)):
    for j in range(i+1,len(x4)):
        if(x4[i]>x4[j]):
            x4[i],x4[j]=x4[j],x4[i]
print(x4)


# In[97]:


x4=[4,76,54,67,90,1000,800,900]
for i in range(len(x4)):
    for j in range(i+1,len(x4)):
        if(x4[i]<x4[j]):
            x4[i],x4[j]=x4[j],x4[i]
print(x4)


# In[99]:


#5.Write a Python program to remove duplicates from a list while maintaining the order of elements.
#a. numbers = [1, 2, 2, 3, 4, 4, 5]
#b. List after removing duplicates: [1, 2, 3, 4, 5]
numbers = [1, 2, 2, 3, 4, 4, 5]
unique=[]
for i in numbers:
    if(i not in unique):
        unique.append(i)
print(unique)


# In[101]:


#6.Write a Python program to find all pairs of numbers in a list that add up to a specific target sum.
#a. numbers = [1, 2, 3, 4, 3, 5, 6] target_sum = 6
#b. Pairs that add up to 6: [(3, 3), (2, 4), (1, 5)]
numbers = [1, 2, 3, 4, 3, 5, 6]
for i in range(len(numbers)):
    for j in range(i+1,len(numbers)):
        if(numbers[i]+numbers[j]==6):
            print(numbers[i],numbers[j])


# In[105]:


numbers = [1, 2, 3, 4, 3, 5, 6]
print(numbers)
numbers.sort()
print(numbers)
start=0
end=len(numbers)-1
while(start<end):
    p=numbers[start]+numbers[end]
    if(p>6):
        end-=1
    elif(p<6):
        start+=1
    else:
        print(numbers[start],numbers[end])
        start+=1
        end-=1


# In[107]:


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


# In[109]:


#8.Write a Python program to find the sum of the elements in a list, excluding the largest and smallest element. Don’t use max or min functions
#a. numbers = [1, 2, 3, 4, 5]
#b. Sum excluding the largest and smallest element: 9
numbers = [1, 2, 3, 4, 5]
maxx=max(numbers)
minn=min(numbers)
summ=0
for i in numbers:
    if(i!=maxx and i!=minn):
        summ+=i
print(summ)


# In[111]:


numbers = [1, 2, 3, 4, 5]
maxx=numbers[0]
minn=numbers[0]
summ=0
for i in range(len(numbers)):
    if(numbers[i]>maxx):
        maxx=numbers[i]
for j in range(len(numbers)):
    if(numbers[j]<minn):
        minn=numbers[j]
for k in range(len(numbers)):
    if(numbers[k]!=maxx and numbers[k]!=minn):
        summ+=numbers[k]
print(summ)


# In[113]:


#11. Find Common Elements in Two Lists
#a. list1 = [1, 2, 3, 4, 5]
#b. list2 = [3, 4, 5, 6, 7]
#c. Result: [3, 4, 5]
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
common=[]
for i in list1:
    for j in list2:
        if(i==j and i not in common):
            common.append(i)
print(common)


# In[117]:


#12. Find the Longest Word in a List
#a. words = ["apple", "banana", "strawberry", "kiwi"]
#b. Strawberry
words = ["apple", "Indian Blackberry", "banana", "strawberry", "kiwi"]
longest=words[0]
for i in range(len(words)):
    if(len(words[i])>len(longest)):
        longest=words[i]
print(longest)


# In[123]:


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


# In[124]:


numbers = [1, 2, 4, 5, 6]
for i in range(len(numbers)-1):
    if((numbers[i+1]-numbers[i])!=1):
        print(numbers[i]+1)



# In[128]:


#15. Find the First Non-Repeating Element
#Given a list of integers, find the first element that appears only once.
#a. numbers = [4, 5, 1, 2, 0, 4, 5, 2]
#b. Expected Output: 1
numbers = [4, 5, 1, 2, 0, 4, 5, 2]
for num in numbers:
    if(numbers.count(num)==1):
        print(num)
        break


# In[129]:


numbers = [4, 5, 1, 2, 0, 4, 5, 2]
for i in range(len(numbers)):
    count=0
    for j in range(len(numbers)):
        if(numbers[i]==numbers[j] and i!=j):
            count+=1
    if(count==0):
        print(numbers[i])
        break



# In[130]:


numbers = [4, 5, 1, 2, 0, 4, 5, 2]
for i in range(len(numbers)):
    count=0
    for j in range(len(numbers)):
        if(numbers[i]==numbers[j] and i!=j):
            count+=1
    if(count==0):
        print(numbers[i])
        break


# In[132]:


numbers = [4, 5, 1, 2, 0, 4, 5, 2]
for i in range(len(numbers)):
    count=0
    for j in range(len(numbers)):
        if(numbers[i]==numbers[j] and i!=j):
            count+=1
    if(count==0):
        print(numbers[i])
        break


# In[134]:


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



# In[135]:


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


# In[143]:


#18. Find Triplets That Sum to Zero
#Given a list of numbers, find all unique triplets (a, b, c) such that a + b + c = 0.
#a. numbers = [-1, 0, 1, 2, -1, -4]
#b. Expected Output: [(-1, -1, 2), (-1, 0, 1)]

numbers = [-1, 0, 1, 2, -1, -4]
new=[]
for i in range(len(numbers)):
    for j in range(i+1,len(numbers)):
        for k in range(j+1,len(numbers)):
            if(numbers[i]+numbers[j]+numbers[k]==0):
                triplets=[numbers[i],numbers[j],numbers[k]]
                triplets.sort()
                if(triplets not in new):
                    new.append((triplets))
print(new)


# In[138]:


numbers = [-1, 0, 1, 2, -1, -4]
new=[]
for i in range(len(numbers)):
    for j in range(i+1,len(numbers)):
        for k in range(j+1,len(numbers)):
            if(numbers[i]+numbers[j]+numbers[k]==0):
                triplets=[numbers[i],numbers[j],numbers[k]]
                triplets.sort()
                if(triplets not in new):
                    new.append(triplets)
print(new)


# In[ ]:




