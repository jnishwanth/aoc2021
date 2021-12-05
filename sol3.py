#!/usr/bin/env python3

from functions import read

def part1(input):
    total = len(input)
    epsilon = [0,0,0,0,0,0,0,0,0,0,0,0]
    gamma = [0,0,0,0,0,0,0,0,0,0,0,0]


    # Setting Gamma
    for line in input:
        for i in range(len(gamma)):
            gamma[i] += int(line[i])
    for i in range(len(gamma)):
        if(gamma[i]>total/2):
            gamma[i]=1
        else:
            gamma[i]=0

    # Setting Epsilon
    for i in range(len(epsilon)):
        if gamma[i]==1:
            epsilon[i] = 0
        else:
            epsilon[i] = 1

    # List to string
    g_str = [str(each) for each in gamma]
    g_str = ''.join(g_str)
    gamma = g_str

    e_str = [str(each) for each in epsilon]
    e_str = ''.join(e_str)
    epsilon = e_str

    # List to Int and Multiply
    print(int(g_str,2)*int(e_str,2))
    return

def part2(input):
    print(int(find_oxygen_rating(input)[0], 2)*int(find_co2_rating(input)[0], 2))
    return

def find_oxygen_rating(input, pos=0):
    if(len(input)==1):
        return input
    input.sort(key=lambda x: x[pos:])
    half = int(len(input)/2)
    input = [item for item in input if item[pos]==input[half][pos]]
    return find_oxygen_rating(input, pos+1)

def find_co2_rating(input, pos=0):
    if(len(input)==1):
        return input
    input.sort(key=lambda x: x[pos:])
    half = int(len(input)/2)
    input = [item for item in input if item[pos]!=input[half][pos]]
    return find_co2_rating(input, pos+1)

def main():
    input = read('inp3')
    part1(input)
    part2(input)
    return

if __name__=='__main__':
    main()
