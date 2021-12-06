#!/usr/bin/env python3
import sys
from functions import get_data
from collections import defaultdict

def main():
    infile  = sys.argv[1] if len(sys.argv)>1 else 'inp5'
    if len(sys.argv)==0:
        get_data(5,2021)
    map1 = defaultdict(int)
    map2 = defaultdict(int)
    with open(infile, 'r') as file:
        for line in file:
            start,end = line.split(' -> ')
            x1,y1 = start.split(',')
            x2,y2 = end.split(',')
            x1 = int(x1)
            y1 = int(y1)
            dx = x1-int(x2)
            dy = y1-int(y2)

            for i in range(1+max(abs(dx),abs(dy))):
                x = x1+(1 if dx<0 else (-1 if dx>0 else 0))*i
                y = y1+(1 if dy<0 else (-1 if dy>0 else 0))*i
                if dx==0 or dy==0:
                    map1[(x,y)] += 1
                map2[(x,y)] += 1

    print(len([k for k in map1 if map1[k]>1]))
    print(len([k for k in map2 if map2[k]>1]))

if __name__=='__main__':
    main()
