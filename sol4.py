#!/usr/bin/env python3

from functions import get_data
import numpy as np
import sys

def to_array():
    infile = sys.argv[1] if len(sys.argv)>1 else 'inp4'
    with open(infile) as file:
        numbers = file.readline().replace('\n', '').split(',')
        cards = [[line.split() for line in card.split('\n')] for card in file.read().split('\n\n')]
    cards[-1].pop(-1)
    cards[0].pop(0)
    return numbers, cards

def check_complete(card):
    checkLine = []
    for i in range(len(card[0])):
        checkLine.append('-1')
    for line in card:
        if(line == checkLine):
            return True
    card = np.transpose(card).tolist()
    for line in card:
        if(line == checkLine):
            return True
    return False

def mark_num(cards, num):
    for i in range(len(cards)):
        for j in range(len(cards[0])):
            for k in range(len(cards[0][0])):
                if(int(num) == int(cards[i][j][k])):
                    cards[i][j][k] = '-1'
    return cards

def calc_score(finNumber, finCard):
    score = 0
    for line in finCard:
        for number in line:
            if(int(number)==-1):
                continue
            score += int(number)
    score *= int(finNumber)
    return score

def delete_card(cards, card):
    for i in range(len(cards)):
        if(cards[i]==card):
            cards.pop(i)
            return cards

def first_card(numbers, cards):
    finCard = []
    finNumber = -1
    for number in numbers:
        cards = mark_num(cards, number)
        for card in cards:
            if(check_complete(card) == True):
                finNumber = number
                finCard = card
                break
        else:
            continue
        break
    return calc_score(finNumber, finCard)

def last_card(numbers, cards):
    for number in numbers:
        cards = mark_num(cards, number)
        for card in cards:
            if(check_complete(card) == True):
                if(len(cards)==1):
                    finNumber = number
                    finCard = card
                    return calc_score(finNumber, finCard)
                cards = delete_card(cards, card)

if __name__ == '__main__':
    #get_data(4,2021)
    numbers, cards = to_array()

    print(first_card(numbers, cards))
    print(last_card(numbers, cards))
