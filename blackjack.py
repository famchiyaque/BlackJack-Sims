# program to simulate blackjack under standar conditions
# simulate winnings/losses throughout entire blackjack stack
# (6 decks) playing by the book
import random
from utils.theBook import theBook
from utils.handReader import handReader
import matplotlib.pyplot as plt

# creating the deck
# deckValues = ['2','3','4','5','6','7','9','10','J','Q','K','A']
# deckSuits = ['H','S','C','D']

# deck = []
# for suit in deckSuits:
#     for value in deckValues:
#         card = value + suit
#         deck.append(card)

# creating the stack
# stack = []
# for card in deck:
#     for i in range(6):
#         stack.append(card)

# random.shuffle(stack)
# print(stack)

def create_shuffled_stack():
    deck_values = ['2','3','4','5','6','7','9','10','J','Q','K','A']
    deck_suits = ['H','S','C','D']
    deck = [value + suit for suit in deck_suits for value in deck_values]
    stack = deck * 6
    random.shuffle(stack)
    return stack

# playerWins = 0
# dealerWins = 0
# ties = 0

# blackjack sim
# round = 1
rounds = []
perctWins = []
# stackLength = len(stack)
# counter = 0
for i in range(0, 100):
    stack = create_shuffled_stack()
    stackLength = len(stack)
    counter = 0
    playerWins = 0
    dealerWins = 0
    ties = 0
    Round = 1
    while(counter <= stackLength - 12):
        # print("Round " + str(Round))
        # print("-----------------------")
        playerHand = stack[counter] + ' ' + stack[counter + 1]
        # print("Player Hand: " + playerHand)
        dealerHand = stack[counter + 2] + ' ?' #+ stack[counter + 3]
        # print("Dealer Hand: " + dealerHand)
        # print('')
        
        pHand = handReader(stack[counter], stack[counter+1])
        dHand = handReader(stack[counter+2], stack[counter+3])
        counter += 4
        # print(pHand)
        # print(dHand)

        result = theBook(pHand, dHand, counter, stack)
        counter = result[2]
        if (result[3] == 1):
            # print("RESULT: player wins 3:1 with blackjack")
            playerWins += 1
        elif (result[4] == 1):
            # print("RESULT: player plays soft and wins 2:1 with blackjack")
            playerWins += 1
        elif (result[5] == 1):
            # print("RESULT: player passed, dealer wins")
            dealerWins += 1
        elif (result[6] == 1):
            # print("RESULT: dealer passed, player wins")
            playerWins += 1
        elif (result[0] > result[1]):
            # print("RESULT: player wins")
            playerWins += 1
        elif (result[1] > result[0]):
            # print("RESULT: dealer wins")
            dealerWins += 1
        else:
            # print("tie")
            ties += 1
        # count -= counter
        Round += 1
        # print('')

    rounds.append(i)
    # print(playerWins)
    # print(dealerWins)
    # print(ties)
    winPerc =  (playerWins/(playerWins+dealerWins+ties))*100
    # print(winPerc)
    winPercFixed = round(winPerc, 1)
    perctWins.append(winPerc)
    counter = 0


average = sum(perctWins)/len(perctWins)
print("Average: ") 
print(round(average, 2))
plt.plot(rounds, perctWins, label='Win Percentage per Round')
plt.axhline(y=average, color='r', linestyle='--', label=f'Average Win Percentage: {average:.2f}%')

# Annotate the average value on the plot
plt.text(rounds[-1], average, f'{average:.2f}%', ha='right', va='bottom', color='red')

# Adding labels and title
plt.xlabel('Round of BJ (Stack of 6 Decks)')
plt.ylabel("'%' of Games Won (each game about 50 rounds)")
plt.title('BlackJack Efficiency (BTB)')

# Adding legend
plt.legend()

# Display the plot
plt.show()
# plt.plot(rounds, perctWins)

# plt.xlabel('Round of BJ (Stack of 6 Decks)')
# plt.ylabel("'%' of Games Won (Each game about 50 rounds)")
# plt.title('BlackJack Efficiency (BTB)')
# plt.axhline(average)
# plt.show()