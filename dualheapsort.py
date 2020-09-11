#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 15:32:31 2019

¡prototype dual-heap sorting algorithm!

slight downfall: user must enter each value individually, which could
be impractical for very large arrays.

in the future, consider file parsing--taking an array directly from a file
and inputting it into the algorithm.

to feed the algorithm random values, uncomment lines 32-33 and comment
lines 30-31.

@author: cosmicchasm1983
"""

import timeit 
import random
import sys

print(""" WELCOME TO THE SORTING ALGORITHM
        RULES: INPUT A SIZE VALUE LARGER THAN 2
        NO FRACTIONAL VALUES ALLOWED
      """)
size = int(input("enter size of list to be sorted: "))

if (size < 3):
    print('execute the program again, and input a size value larger than 2.')
    sys.exit()

values = [] #initializing integral algorithm components
    
maxvalues = []

sorted_list = []

for i in range(0,size): #appending initial values
    values.append(int(input(f'enter list value no. {i+1}: ')))

#for i in range(0,size):
#    values.append(random.randint(0,1000))

timerstart = timeit.default_timer() 
for i in range(0,int((size/2))+1): 
    if len(sorted_list) < (len(values) - 1): #boundaries
        maxvalues.append(max(values)) #removing max values
        values.remove(max(values))
    sorted_list.append(min(values)) 
    values.remove(min(values))
    #lines 36-37 are the backbone of the conventional heap algorithm
for element in list(reversed(maxvalues)): 
    sorted_list.append(element) #layering sorted max values onto sorted mins
timerend = timeit.default_timer()

elapsed = timerend - timerstart #rough method of deriving the amount of time taken

print(sorted_list) #et voila
print('successfully sorted.')
print(f'\nprocess took {elapsed} seconds.')

