#!/usr/bin/env python3
import sys
from functions import get_data

infile = sys.argv[1] if len(sys.argv)>1 else 'inp2'
inpu =[[line.replace('\n','').split()[0], int(line.replace('\n','').split()[1])] for line in open(infile).readlines()]

def location1():
    horizontal = 0
    depth = 0
    for command in inpu:
        if(command[0]=='forward'):
            horizontal+=int(command[1])
        elif(command[0]=='down'):
            depth+=int(command[1])
        else:
            depth-=int(command[1])
    print(depth*horizontal)
    return depth*horizontal

def location2():
    aim = 0
    depth = 0
    horizontal = 0
    for command in inpu:
        if(command[0]=='forward'):
            horizontal += int(command[1])
            depth += aim*int(command[1])
        elif(command[0]=='up'):
            aim -= int(command[1])
        else:
            aim += int(command[1])
    print(depth*horizontal)
    return depth*horizontal

if __name__=='__main__':
    get_data(2,2021)

    location1()
    location2()
