#!/usr/bin/env python3
import requests as r
from aoc_cookie import get_cookie as get_cookie

def read(inpu):
    out = []
    with open(inpu,'r') as inp:
        while(line := inp.readline().rstrip()):
            out.append(line)
    return(out)

def get_data(day, year):
    url = f'https://adventofcode.com/{year}/day/{day}/input'
    resp = r.get(url, headers={
        'Cookie': f'{get_cookie()}',
    })
    with open(f'inp{day}','w') as data:
        data.write(resp.text)
    return resp.text
