# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 09:39:33 2022

@author: PVS DELL
"""

### Q(3)

print("==== Q(3) ANSWER =======")
L1 = [0,1,2,3,4,5,6,7,8,9,10]
print(L1[:-1])

### Q(4)

print("==== Q(4) ANSWER =======")
print("Python" > "python")

### Q(6)
print("==== Q(6) ANSWER =======")
import keyword
def is_valid_identifier(s):
    return s.isidentifier() and not keyword.iskeyword(s)

identifier_list = ['_', '798', 'for', 'a**2']

for s in identifier_list:
    print("Identifier %s is %s" %(s, is_valid_identifier(s)))
    
### Q(7)
print("==== Q(7) ANSWER =======")
my_dictionary= {1: "John", 1: "Benny", 1: "Abbot", 2: "Sameul"}
print(my_dictionary)

### Q(9)
print("==== Q(9) ANSWER =======")
my_list = ["B", "C", "D", "E", "F"]
my_list.insert(0, "A")
print(my_list)

### Q(14)
print("==== Q(14) ANSWER =======")
email_list = ['aaron.w@gmail.com', 'benny.w@hotmail.com', 'charles.W@gmail.com', 'benny.w@hotmail.com',\
              'aaron.w@gmail.com', 'benny.w@hotmail'] 
email_list_set = list(set(email_list))
print(len(email_list_set))
 
### Q(15)
print("==== Q(15) ANSWER =======")
string = "Fruits such as berries, cherries, plumns, grapefruit, peaches, apples, pears and oranges are lower on glycemic index"
s = (string.split(',', maxsplit = 4))
print(s[-2])

### Q(18)
print("==== Q(18) ANSWER =======")

print(162/ 3 + (1+1)**3)
    
    


