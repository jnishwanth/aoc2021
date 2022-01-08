#!/usr/bin/env python3
import sys
from functions import get_data
from pprint import pprint

def glow(octopi, glows):
    moveArr = [[-1,0], [-1,1], [0,1], [1,1], [1,0], [1,-1], [0,-1], [-1,-1]]
    for i in range(len(octopi)):
        for j in range(len(octopi[0])):
            if(octopi[i][j]==9):
                octopi[i][j] = 0
                glows += 1
                for k in range(len(moveArr)):
                    x = i + moveArr[k][0]
                    y = j + moveArr[k][1]
                    if(0<=x<len(octopi) and 0<=y<len(octopi[0]) and octopi[x][y]!=0):
                        octopi[x][y] += 1
    return octopi


if __name__=='__main__':
    # get_data(11,2021)
    glows = 0
    infile = sys.argv[1] if len(sys.argv)>1 else 'testcase'
    octopi = [[int(octopus) for octopus in line.replace('\n','')] for line in open(infile)]
    for count in range(1):
        for line in octopi:
            for i in range(len(line)):
                line[i] += 1

        while (max(max(line) for line in octopi)>=9):
            glow(octopi, glows)

    print(f'{glows}\n')
    print('\n'.join([''.join(['{:3}'.format(item) for item in row])for row in octopi]))
