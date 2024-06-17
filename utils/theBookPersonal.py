# code for: THE BOOK
def theBook(cardP1, cardP2, dealer):
    pHTotal = cardP1 + cardP2
    cardD1 = dealer

    # when player has a pair
    if (pHTotal == 21):
        print("you have blackjack, play soft")
    elif (cardP1 == cardP2):
        # player splits
        if (((cardP1 == 2 or cardP1 == 3) and (4 <= cardD1 <= 7)) or (cardP1 == 6 and cardD1 <= 6) or (cardP1 == 7 and cardD1 <= 7) or (cardP1 == 9 and (cardD1 >= 6 or 8 <= cardD1 <= 9)) or (cardP1 == 8 or cardP1 == 11)):
            print("split with pair of " + str(cardP1) + 's against dealer ' + str(cardD1))

        # player hits on pair
        elif (((cardP1 == 2 or cardP1 == 3) and (cardD1 <= 3 or cardD1 >= 8)) or (cardP1 == 4) or (cardP1 == 5 and cardD1 >= 10) or (cardP1 == 6 and cardD1 >= 7) or (cardP1 == 7 and cardD1 >= 8)):
            print("hit on pair of " + str(cardP1) + 's against dealer ' + str(cardD1))

        # player stands on pair
        elif (cardP1 == 10 or (cardP1 == 9 and (cardD1 == 7 or cardD1 >= 10))):
            print("stand on pair of " + str(cardP1) + 's against dealer ' + str(cardD1))
        
        # player doubles with 5s against dealer <= 9
        elif (cardP1 == 5 and cardD1 <= 9):
            print("double bet with pair of 5s against dealer " + str(cardD1))
            
    # when player has an ace
    elif (cardP1 == 11 or cardP2 == 11):
        # player hits with ace in hand
        if ((pHTotal <= 17 and (cardD1 <= 3 or cardD1 >= 7)) or (pHTotal == 18 and (cardD1 >= 9))):
            print("hit with ace in hand and total " + str(pHTotal) + " against dealer " + str(cardD1))
                
        # player stands with ace in hand
        elif (((pHTotal == 18) and (cardD1 == 2 or cardD1 == 7 or cardD1 == 8)) or (19 <= pHTotal <= 20)):
            print("stand with ace in hand with total " + str(pHTotal) + " de a huevo against dealer " + str(cardD1))
                
        # player doubles with ace in hand
        elif ((13 <= pHTotal <= 18 and 4 <= cardD1 <= 6) or (pHTotal == 18 and cardD1 == 3)):
            print("double with ace in hand and total " + str(pHTotal) + " against dealer " + str(cardD1))
    
    # normal circumstances
    else:
        # player hits
        if ((pHTotal <= 8) or (pHTotal == 9 and (cardD1 == 2 or cardD1 >= 7)) or (pHTotal == 10 and cardD1 >= 10) or (pHTotal == 12 and (2 <= cardD1 <= 3 or cardD1 >= 7)) or (13 <= pHTotal <= 16 and cardD1 >= 7)):
            print("hit with " + str(pHTotal) + " against dealer " + str(cardD1))

        # player stands
        elif ((pHTotal >= 17) or (13 <= pHTotal <= 16 and cardD1 <= 6) or (pHTotal == 12 and 4 <= cardD1 <= 6)):
            print("stand with " + str(pHTotal) + " against dealer " + str(cardD1))

        # player doubles
        elif((pHTotal == 9 and 3 <= cardD1 <= 6) or (pHTotal == 10 and 2 <= cardD1 <= 9) or (pHTotal == 11)):
            print("double bet with total " + str(pHTotal) + " against dealer " + str(cardD1))

def theBook2(total, dealer):
    pHTotal = total
    cardD1 = dealer

    # normal circumstances
    # player hits
    if ((pHTotal <= 8) or (pHTotal == 9 and (cardD1 == 2 or cardD1 >= 7)) or (pHTotal == 10 and cardD1 >= 10) or (pHTotal == 12 and (2 <= cardD1 <= 3 or cardD1 >= 7)) or (13 <= pHTotal <= 16 and cardD1 >= 7)):
        print("hit with " + str(pHTotal) + " against dealer " + str(cardD1))

    # player stands
    elif ((pHTotal >= 17) or (13 <= pHTotal <= 16 and cardD1 <= 6) or (pHTotal == 12 and 4 <= cardD1 <= 6)):
        print("stand with " + str(pHTotal) + " against dealer " + str(cardD1))

   # player doubles
    elif((pHTotal == 9 and 3 <= cardD1 <= 6) or (pHTotal == 10 and 2 <= cardD1 <= 9) or (pHTotal == 11)):
        print("double bet with total " + str(pHTotal) + " against dealer " + str(cardD1))
