"""
Created on Thu Jun 20 15:32:31 2019

test script for the dual-heap algorithm
DECOMMISSIONED

simply run the program to witness its magic

trial is constituted of feeding 100 arrays of 1000 random values from 0
to 10000 (identical for each algorithm) and measuring the average amount of
time it takes for each algorithm to sort the individual arrays.

sort = dual heap

@author: cosmicchasm1983
"""

import timeit 
import random
import time

heapsum = 0
sortsum = 0

#conventional heap sort algorithm
#draws mins from an array, appends them sorted to another

for i in range(0,100):
    
    sort = values = []
    #values = []
    sorted_values = []
    for i in range(0,1000):
        sort.append(random.randint(0,10000))
        #values = sort
        #print(values)
    values = sort.copy()
    #print(values)
    timestart = timeit.default_timer()
    for i in range(0,1000):
        sorted_values.append(min(sort))
        sort.remove(min(sort))
    timeend = timeit.default_timer()

    elapser = timeend - timestart

#___________________________________________________________________________
#modified heap sort -- dual-heap
#takes both mins and maxes, appends them into arrays, then rotates the max
#and appends to the mins
    
    maxvalues = []

    sorted_list = []

    #for i in range(0,1000):
        #values.append(random.randint(0,10000))

    timerstart = timeit.default_timer() 
    for i in range(0,int((1000/2))+1): 
        if len(sorted_list) < (len(values) - 1):
            maxvalues.append(max(values))
            values.remove(max(values))
        sorted_list.append(min(values))
        values.remove(min(values))
    for element in list(reversed(maxvalues)): 
        sorted_list.append(element)
    timerend = timeit.default_timer()

    elapsed = timerend - timerstart

    heapsum += elapser
    sortsum += elapsed
    #print(f'process {j+1} successful.')
    #time.sleep(0.00001)
heapaverage = heapsum / 100
sortaverage = sortsum / 100

print(f'\nheap average = {heapaverage} seconds')
print(f'\nsort average = {sortaverage} seconds')
