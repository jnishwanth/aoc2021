#!/usr/bin/env python3
from functions import get_data
import sys

infile = sys.argv[1] if len(sys.argv)>1 else 'inp7'

def main():
    crabs = [int(crab) for crab in open(infile).read().replace('\n', '').split(',')]
    ans1 = min( [ sum([ abs(crab-k) for crab in crabs ]) for k in [i for i in range(max(crabs)+1)] ]   )
    ans2 = min( [ sum([ int(abs(crab-k)*(abs(crab-k)+1)/2) for crab in crabs ]) for k in [i for i in range(max(crabs)+1)] ]   )
    print(ans1)
    print(ans2)

if __name__=='__main__':
    get_data(7,2021)
    main()
