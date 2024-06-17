import random
from utils.theBookPersonal import theBook
from utils.theBookPersonal import theBook2
import matplotlib.pyplot as plt

# creating the deck
deckValues = ['2','3','4','5','6','7','9','10','J','Q','K','A']
deckSuits = ['H','S','C','D']

deck = []
for suit in deckSuits:
    for value in deckValues:
        card = value + suit
        deck.append(card)

# creating the stack
stack = []
for card in deck:
    for i in range(6):
        stack.append(card)

random.shuffle(stack)
# print(stack)

counter = 0
wins = 0
losses = 0
ties = 0

def hit(counter, total):
    nextCard = stack[counter]
    counter += 1
    print("Next Card: " + nextCard)
    newValue = convertNextCard(nextCard[0])
    total += newValue
    print("New Total: " + str(total))
    return [counter, total]

def double(counter, total):
    nextCard = stack[counter]
    counter += 1
    print("Next Card: " + nextCard)
    newValue = convertNextCard(nextCard[0])
    total += newValue
    print("New Total: " + str(total))
    return [counter, total]

def split(counter):
    firstCard = stack[counter]
    counter += 1
    print("First card: " + firstCard)
    again = input("Hit Again? ")
    while (again != "no"):
        counter = hit(counter)
        again = input("Hit Again? ")
    return counter

def convertNextCard(card):
    if (card == 'A'):
        card = 11
    elif (card == '1' or card == 'J' or card == 'Q' or card == 'K'):
        card = 10
    else:
        card = int(card)
    return card

def convertHand(card1, card2):
    card1 = card1[0]
    if (card1 == 'A'):
        card1 = 11
    elif (card1 == '1' or card1 == 'J' or card1 == 'Q' or card1 == 'K'):
        card1 = 10
    else:
        card1 = int(card1)
    card2 = card2[0]
    if (card2 == 'A'):
        card2 = 11
    elif (card2 == '1' or card2 == 'J' or card2 == 'Q' or card2 == 'K'):
        card2 = 10
    else:
        card2 = int(card2)
    return [card1, card2]

chips = 1000
runningCount = 0
trueValue = 0
decksLeft = 6

for i in range(100):
    print("Running Count: " + str(runningCount))
    print("Chip count: " + str(chips))
    bet = int(input("What's your bet? "))

    card1 = stack[counter]
    card2 = stack[counter+1]
    print("Hand: " + card1 + ', ' + card2)
    counter += 2

    hand = convertHand(card1, card2)
    card1 = hand[0]
    card2 = hand[1]
    total = card1 + card2
    print("Total: " + str(total))

    dealer = int(input("What does the dealer have? "))

    decision = ''

    if (total < 17):
        hint = input("Do you want a hint? ")
        if (hint == "yes"):
            theBook(card1, card2, dealer)
        decision = input("Your Move: ")
        while (decision != "stand" and decision != 'bust'):
            if (decision == "hit"):
                result = hit(counter, total)
                counter = result[0]
                total = result[1]
                if (total >= 17):
                    break
                else:
                    decision = input("Your Move: ")
            elif (decision == "split"):
                counter = split(counter)
            elif (decision == 'double'):
                bet = bet*2
                result = double(counter, total)
                counter = result[0]
                total = result[1]
                if (total >= 17):
                    break
                else:
                    decision = input("Your Move: ")

    result = input("What was the result? (win/loss/tie) ")

    if (decision == 'bust'):
        losses += 1
        chips = chips - bet
    else:
        if (result == 'win'):
            wins += 1
            chips = chips + bet
        elif (result == 'loss'):
            losses += 1
            chips = chips - bet
        elif (result == 'bj' or result == 'blackjack'):
            wins += 1
            chips = chips + bet*1.5
        else:
            ties += 1

    # ones = int(input("How many ones? "))
    # minusOnes = int(input("How many tens? "))
    # runningCount = runningCount + (ones - minusOnes)
    runningCount = int(input("What's the new running count? "))
    print("-------------------")