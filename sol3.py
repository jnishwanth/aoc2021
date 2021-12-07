#!/usr/bin/env python3
import sys
from functions import get_data
from numpy import zeros

def part1(inpu):
    total = len(inpu)
    epsilon = zeros(12, int)
    gamma = zeros(12, int)

    # Setting Gamma
    for line in inpu:
        for i in range(len(gamma)):
            gamma[i] += int(line[i])
    for i in range(len(gamma)):
        if(int(gamma[i])>total/2):
            gamma[i] = 1
        else:
            gamma[i] = 0

    # Setting Epsilon
    for i in range(len(epsilon)):
        if gamma[i]==1:
            epsilon[i] = 0
        else:
            epsilon[i] = 1

    # List to string
    gamma = ''.join([str(each) for each in gamma])
    epsilon = ''.join(str(each) for each in epsilon)

    # List to Int and Multiply
    return (int(gamma,2)*int(epsilon,2))

def find_oxygen_rating(inpu, pos=0):
    if(len(inpu)==1):
        return inpu
    inpu.sort(key=lambda x: x[pos:])
    half = int(len(inpu)/2)
    inpu = [item for item in inpu if item[pos]==inpu[half][pos]]
    return find_oxygen_rating(inpu, pos+1)

def find_co2_rating(inpu, pos=0):
    if(len(inpu)==1):
        return inpu
    inpu.sort(key=lambda x: x[pos:])
    half = int(len(inpu)/2)
    inpu = [item for item in inpu if item[pos]!=inpu[half][pos]]
    return find_co2_rating(inpu, pos+1)

if __name__=='__main__':
    infile = sys.argv[1] if len(sys.argv)>1 else 'inp3'
    inpu = [line.replace('\n','') for line in open(infile)]
    print(part1(inpu))
    print(int(find_oxygen_rating(inpu)[0], 2)*int(find_co2_rating(inpu)[0], 2))
