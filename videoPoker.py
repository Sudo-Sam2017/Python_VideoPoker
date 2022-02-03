#Video Poker

import random, sys
from collections import Counter

HEARTS = chr(9829)
DIAMONDS = chr(9830)
SPADES = chr(9824)
CLUBS = chr(9827)

flop = []
suitList = []

def main():
    print('Welcome User!')
    answer = input("Would you like to play?  ")
    if answer == 'Yes':
        newFlop = displayFlop()
        flop = newFlop
        discardRedraw(flop)
    else:
        sys.exit()

def buildDeck():
    deck = []
    for suit in (HEARTS, DIAMONDS, SPADES, CLUBS):
        for rank in range(2, 11):
            deck.append((str(rank), suit))
        for rank in ('A', 'K', 'Q', 'J'):
            deck.append((rank, suit))
    random.shuffle(deck)
    return deck


def removeOneZero(cardList):
    if '0' in cardList:
        cardList.remove('0')
    else:
        pass
    
    if '1' in cardList:
        index = cardList.index('1')
        cardList.pop(index)
        cardList.insert(index, '10')
    else:
        pass

def discardRedraw(flop):
    playerHand = []
    playerHand = flop
    decision = input('Would you like to discard any of your cards? ')
    if decision == 'y':
        discardCard = int(input("Which card would you like to discard? (Enter 0 through 4) "))
        print(playerHand[0][discardCard], playerHand[1][discardCard])
    else:
        checkforPair(flop)
        checkTwoPair(flop)
        checkThreeOfAKind(flop)
        checkFourOfAKind(flop)




def displayFlop():
     flop = []
     suitList = []
     deck = buildDeck()
     for x in range(0, 5):
        newCard = deck.pop()
        rank, suit = newCard
        print('You drew a {} of {}.'.format(rank, suit))
        rankNum = rank
        suitType = suit
        flop += rankNum
        suitList += suitType
     removeOneZero(flop)
     print(suitList)
     return flop, suitList


def checkforPair(flop):
     cardSet = set(flop)
     containsDuplicates = len(flop) != len(cardSet)
     if containsDuplicates:
         print("You have a pair!")
         #Error: will not display message when a pair of 10s come on the flop
     else:
         print('No pairs')

def checkTwoPair(flop):
    doubles = []
    for k, v in Counter(flop).items():
        doubles.extend([k] * ( v // 2))
    numPairs = len(doubles)
    if numPairs == 2:
        print("You have two pair!!")
    else:
        pass   

def checkThreeOfAKind(flop):
    triples = []
    for k, v in Counter(flop).items():
        triples.extend([k] * (v // 3))
    numTrips = len(triples)
    if numTrips >= 1:
        print("You have three of a kind!")
    else:
        pass

def checkFourOfAKind(flop):
    quads = []
    for k, v in Counter(flop).items():
        quads.extend([k] * (v // 4))
    numQuads = len(quads)
    if numQuads >= 1:
        print("You have four of a kind!")
    else:
        pass

def checkFlush(suitList):
    result = all(element == suitList[0] for element in suitList)
    if (result):
        print("You have a flush!!")
    else:
        pass

   

if __name__ == '__main__':
    main()