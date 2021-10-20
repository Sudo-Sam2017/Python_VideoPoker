import random, sys

HEARTS = chr(9829)
DIAMONDS = chr(9830)
SPADES = chr(9824)
CLUBS = chr(9827)


def main():
    print('Welcome User!')
    answer = input("Would you like to play?  ")
    if answer == 'Yes':
        checkforPair()
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
        cardList.remove('1')
        cardList.append('10')
    else:
        pass


def checkforPair():
     flop = []
     physicalCards = []
     deck = buildDeck()
     for x in range(0, 5):
        newCard = deck.pop()
        rank, suit = newCard
        print('You drew a {} of {}.'.format(rank, suit))
        rankNum = rank
        flop += rankNum
        physicalCards += newCard
     removeOneZero(flop)
     cardSet = set(flop)
     containsDuplicates = len(flop) != len(cardSet)
     if containsDuplicates:
         print("You have a pair!")
     else:
         print('No pairs')
   

if __name__ == '__main__':
    main()