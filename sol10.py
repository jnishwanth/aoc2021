#!/usr/bin/env python3
import sys
from functions import get_data

if __name__=='__main__':
    get_data(10,2021)
    infile = sys.argv[1] if len(sys.argv)>1 else 'inp10'
    subsystem = [line.replace('\n','') for line in open(infile)]
    pairs = {
        '(': ')',
        '[': ']',
        '{': '}',
        '<': '>',
    }
    socres1 = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137,
    }
    scores2 = {
        '(': 1,
        '[': 2,
        '{': 3,
        '<': 4,
    }
    new = set(subsystem)
    ans1 = 0
    ans2 = []
    for line in new:
        stack = []
        for i in range(len(line)):
            if (line[i] in pairs.keys()):
                stack.append(line[i])
            elif (line[i] in pairs.values()):
                if (line[i] == pairs[stack[-1]]):
                    stack.pop()
                else:
                    ans1 += socres1[line[i]]
                    subsystem.remove(line)
                    del stack[:]
                    break
        tmp = 0
        while(len(stack)>0):
            tmp = tmp*5 + scores2[stack.pop()]
        if tmp>0: ans2.append(tmp)
    print(ans1)
    print(sorted(ans2)[int(len(ans2)/2)])
