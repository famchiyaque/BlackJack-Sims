# algorithm to get card values for each card for each hand
def handReader(card1, card2):
    # print(card1, len(card1))
    # print(card2, len(card2))
    cardValue1 = 0
    cardValue2 = 0
    if (card1[0] == '1' or card1[0] == 'J' or card1[0] == 'Q' or card1[0] == 'K'):
        # card1[0] = 10
        cardValue1 = 10
    elif (card1[0] == 'A'):
        cardValue1 = 11
    else:
        cardValue1 = int(card1[0])

    if (card2[0] == '1' or card2[0] == 'J' or card2[0] == 'Q' or card2[0] == 'K'):
        # card2[0] = 10
        cardValue2 = 10
    elif (card2[0] == 'A'):
        cardValue2 = 11
    else:
        cardValue2 = int(card2[0])

    totalValue = str(cardValue1 + cardValue2)

    # print("Values of " + user + " hand: " + card1[0] + ' ' + card2[0])
    # print("Total Value: " + totalValue)
    return [cardValue1, cardValue2]