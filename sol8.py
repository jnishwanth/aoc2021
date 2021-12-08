#!/usr/bin/env python3
import sys
from functions import get_data
from collections import defaultdict

segments = defaultdict(str)
total = 0
def get_key(value, segments=segments):
    return list(segments.keys())[list(segments.values()).index(value)]

def str_add(str1, str2):
    tmp = ''
    for letter in str(str2):
        if letter not in str1:
            tmp += letter
    return ''.join(sorted(str1+tmp))

if __name__=='__main__':
    get_data(8,2021)
    infile = sys.argv[1] if len(sys.argv)>1 else 'inp8'
    inNum = [[''.join(sorted(digit)) for digit in line.split(' | ')[0].replace('\n','').split(' ')] for line in open(infile).readlines()]
    outNum = [[''.join(sorted(digit)) for digit in line.split(' | ')[1].replace('\n','').split(' ')] for line in open(infile).readlines()]
    unique = 0
    i = 0
    for line in inNum:
        for digit in line:
            if(len(digit)==2):
                segments[1] = digit
            elif(len(digit)==4):
                segments[4] = digit
            elif(len(digit)==3):
                segments[7] = digit
            elif(len(digit)==7):
                segments[8] = digit

        for digit in line:
            if(len(digit)==5 and len(str_add(digit, segments[1])) == 5):
                segments[3] = digit
            elif(len(digit)==6 and len(str_add(digit, segments[1])) == 7):
                segments[6] = digit

        for digit in line:
            if(digit in segments.values()):
                continue
            if(len(digit)==6 and len(str_add(digit, segments[3])) == 6):
                segments[9] = digit
            elif(len(digit)==5 and len(str_add(digit, segments[4])) == 6):
                segments[5] = digit

        for digit in line:
            if(digit in segments.values()):
                continue
            if(len(digit)==6):
                segments[0] = digit
            elif(len(digit)==5):
                segments[2] = digit

        deocodedVal = ''.join([str(list(segments.keys())[list(segments.values()).index(digit)]) for digit in outNum[i]])
        total += int(deocodedVal)
        i+=1
        segments = defaultdict(int)
    print(total)
