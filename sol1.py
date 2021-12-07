#!/usr/bin/env python3
from functions import get_data
import sys

get_data(1,2021)
infile = sys.argv[1] if len(sys.argv)>1 else 'inp1'
count1 = count2 = 0

inpu = [int(depth) for depth in open(infile).read().split()]

for i in range(len(inpu)-1):
    if(inpu[i]<inpu[i+1]):
        count1+=1

for i in range(len(inpu)-3):
    if(inpu[i]<inpu[i+3]):
        count2+=1

print(count1)
print(count2)
