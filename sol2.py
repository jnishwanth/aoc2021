#!/usr/bin/env python3

from functions import read

input = read('inp2')

def location1():
    horizontal = 0
    depth = 0
    for command in input:
        if(command.split()[0]=='forward'):
            horizontal+=int(command.split()[1])
        elif(command.split()[0]=='down'):
            depth+=int(command.split()[1])
        else:
            depth-=int(command.split()[1])
    print(depth*horizontal)
    return depth*horizontal

def location2():
    aim = 0
    depth = 0
    horizontal = 0
    for command in input:
        if(command.split()[0]=='forward'):
            horizontal += int(command.split()[1])
            depth += aim*int(command.split()[1])
        elif(command.split()[0]=='up'):
            aim -= int(command.split()[1])
        else:
            aim += int(command.split()[1])
    print(depth*horizontal)
    return depth*horizontal

def main():
    location1()
    location2()
    return

if __name__=='__main__':
    main()
