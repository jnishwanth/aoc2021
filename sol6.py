#!/usr/bin/env python3
import sys
from functions import get_data
from collections import defaultdict

infile = sys.argv[1] if len(sys.argv)>1 else 'inp6'

def fish_count(days):
    fishes = defaultdict(int)

    for i in open(infile).read().replace('\n', '').split(','):
        fishes[int(i)] += 1

    for i in range(days):
        tmp = fishes[0]
        for i in range(8):
            fishes[i] = fishes[i+1]
        fishes[8] = tmp
        fishes[6] += tmp

    print(sum(fishes.values()))

if __name__=='__main__':
    get_data(6,2021)

    fish_count(256)
