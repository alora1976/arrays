# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 11:28:12 2019

@author: Lori
"""

#array

my_list = [2,4,6,8,10] #creates an array called my_list
print(my_list)#prints the array called my_list
print("\n")#creates a space between lines of code so this is easier to follow

my_list[3]=100#replaces index 3 that has a value of 8 with the value of 100
print(my_list)#prints updated my_list
print("\n")#creates a space between lines of code so this is easier to follow

for number in my_list:#traversing array using a for loop
    print(number)#prints numbers in my_list
print("\n")#creates a space between lines of code so this is easier to follow
    
for index in range (len(my_list)):#traversing an array using len and range functions using index
    print(my_list[index])
print("\n")#creates a space between lines of code so this is easier to follow

index=0
length = len(my_list)#traversing an array using a while loop
while index<length:
    print(my_list[index])
    index += 1
print("\n")#creates a space between lines of code so this is easier to follow
    
for index, number in enumerate(my_list):#using enumerate function travberse array and print index as well as number within each index
    print(index,number)
print("\n")#creates a space between lines of code so this is easier to follow    

my_list.insert(3,12)#insert value into an array at index using insert method
print(my_list)
print("\n")#creates a space between lines of code so this is easier to follow

my_list.append(12)#using the append method adds object to end of list
print(my_list)

try:
    my_list.remove(6)#deleteing an element from an array based on the value of that element
except:
    print("Element not Found")#exception created just in case the element is not found in the array
print(my_list)
print("\n")#creates a space between lines of code so this is easier to follow

del(my_list[3])#deletes element from array using del function and index of element in the array
print(my_list)
print("\n")#creates a space between lines of code so this is easier to follow

pop_value = my_list.pop(3)#delete an element in an array using pop method
print(pop_value)
print(my_list)
print("\n")#creates a space between lines of code so this is easier to follow

#searching an array

my_list=[2,4,6,8,10,8,6,4,2]#creates a new array called my_list
print(my_list)#prints new array
for index, number in enumerate(my_list):#searches an array for first instance of element,notice there is another 6 at index 6
    if number==6:
        break
    if index==len(my_list) -1:
        index+= 1
if index<len(my_list):
    print("Item Found at Index", index )
else:
    print("Item not Found")
print("\n")#creates a space between lines of code so this is easier to follow

try:
    index=my_list.index(6)
    print("Item Found at Index",index)
except:
    print("Item not Found")
print("\n")#creates a space between lines of code so this is easier to follow    
if 6 in my_list:
    print("Item Found")
else:
    print("Item not Found")
print("\n")#creates a space between lines of code so this is easier to follow

boolean_list = [6== number for number in my_list]
print(boolean_list)
print("\n")#creates a space between lines of code so this is easier to follow