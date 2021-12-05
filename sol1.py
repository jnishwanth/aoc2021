#!/usr/bin/env python3

from functions import read

init_depth = 0
count = 0

inpu = read('inp1')

for i in range(len(inpu)-3):
    if(inpu[i]<inpu[i+3]):
        count+=1
print(count)
