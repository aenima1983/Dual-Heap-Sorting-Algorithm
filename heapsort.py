#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 15:23:10 2019

heap sort algorithm

to fill the array with 'size' random values, uncomment lines 17-18 and comment
lines 21-22.

@author: cosmicchasm1983
"""
import timeit
import random

sort = []
sorted_values = []

print("INPUT A SIZE VALUE LARGER THAN TWO!!")

size = int(input("enter the size of the array to be sorted: "))
#for i in range(0,size):
    #sort.append(random.randint(0,10000))

for i in range(0,size):
    sort.append(int(input(f"enter value no. {i+1}: ")))

timestart = timeit.default_timer()
for i in range(0,size):
    sorted_values.append(min(sort))
    sort.remove(min(sort))
timeend = timeit.default_timer()

elapser = timeend - timestart

print(sorted_values)
print(f"algorithm took {elapser} seconds to sort the array.")
#______________________________________________________________________________




