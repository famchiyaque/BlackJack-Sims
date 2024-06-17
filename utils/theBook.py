# code for: THE BOOK
def theBook(pHand, dHand, counter, stack):
    # print("current counter: " + str(counter))
    cardP1 = pHand[0]
    cardP2 = pHand[1]
    cardD1 = dHand[0]
    cardD2 = dHand[1]
    pHTotal = sum(pHand)
    dHTotal = sum(dHand)
    bjClean = 0
    bjDirty = 0
    playerPassed = 0
    dealerPassed = 0

    # when player has a pair
    if (pHTotal == 21):
        # print("player has blackjack")
        
        if (dHTotal == 21):
            # print("dealer has blackjack")
            # print("player plays soft and wins 2:1 with blackjack")
            bjDirty = 1
        else:
            # print("player wins 3:1 with blackjack")
            bjClean = 1
        return [pHTotal, dHTotal, counter, bjClean, bjDirty, playerPassed, dealerPassed]
    elif (cardP1 == cardP2):
        # player splits
        if (((cardP1 == 2 or cardP1 == 3) and (4 <= cardD1 <= 7)) or (cardP1 == 6 and cardD1 <= 6) or (cardP1 == 7 and cardD1 <= 7) or (cardP1 == 9 and (cardD1 >= 6 or 8 <= cardD1 <= 9)) or (cardP1 == 8 or cardP1 == 11)):
            # print("player splits here with pair of: " + str(cardP1) + 's against dealer ' + str(cardD1))
            # print("player now has two hands with " + str(cardP1))
            # print("first hand hit is " + str(stack[counter]))
            firstHit = stack[counter][0]
            if (firstHit == '1' or firstHit == 'J' or firstHit == 'Q' or firstHit == 'K'):
                firstHit = 10
            elif (firstHit == 'A'):
                if (pHTotal + 11 > 21):
                    firstHit = 1
                elif (pHTotal + 11 <= 21):
                    firstHit = 11
            else:
                firstHit = int(firstHit)
            pHTotal += firstHit
            # print("first hand total: " + str(cardP1 + firstHit))
            counter += 1
            # print("second hand hit is " + str(stack[counter]))
            secondHit = stack[counter][0]
            if (secondHit == '1' or secondHit == 'J' or secondHit == 'Q' or secondHit == 'K'):
                secondHit = 10
            elif (secondHit == 'A'):
                if (pHTotal + 11 > 21):
                    secondHit = 1
                elif (pHTotal + 11 <= 21):
                    secondHit = 11
            else:
                secondHit = int(secondHit)
            pHTotal += secondHit
            # print("second hand total: " + str(cardP1 + secondHit))
            counter += 1

        # player hits on pair
        elif (((cardP1 == 2 or cardP1 == 3) and (cardD1 <= 3 or cardD1 >= 8)) or (cardP1 == 4) or (cardP1 == 5 and cardD1 >= 10) or (cardP1 == 6 and cardD1 >= 7) or (cardP1 == 7 and cardD1 >= 8)):
            while(pHTotal <= 17):
                # print("player hits on pair of " + str(cardP1) + 's' + " against dealer " + str(cardD1))
                # print("next card is " + str(stack[counter]))

                nextValue = stack[counter][0]
                if (nextValue == '1' or nextValue == 'J' or nextValue == 'Q' or nextValue == 'K'):
                    nextValue = 10
                elif (nextValue == 'A'):
                    if (pHTotal + 11 > 21):
                        nextValue = 1
                    elif (pHTotal + 11 <= 21):
                        nextValue = 11
                else:
                    nextValue = int(nextValue)
                pHTotal += nextValue
                # print("new player total: " + str(pHTotal))
                counter += 1
        # player stands on pair
        elif (cardP1 == 10 or (cardP1 == 9 and (cardD1 == 7 or cardD1 >= 10))):
            # print("player stands on pair of " + str(cardP1) + 's' + " against dealer " + str(cardD1))
            randomValue = 0
        # player doubles with 5s against dealer <= 9
        elif (cardP1 == 5 and cardD1 <= 9):
            # print("player doubles with pair of 5s against dealer " + str(cardD1))
            # print("next card is " + str(stack[counter]))
            nextValue = stack[counter][0]
            if (nextValue == '1' or nextValue == 'J' or nextValue == 'Q' or nextValue == 'K'):
                nextValue = 10
            elif (nextValue == 'A'):
                if (pHTotal + 11 > 21):
                    nextValue = 1
                elif (pHTotal + 11 <= 21):
                    nextValue = 11
            else:
                nextValue = int(nextValue)
            pHTotal += nextValue
            # print("new player total: " + str(pHTotal))
            counter += 1
            
    # when player has an ace
    elif (cardP1 == 11 or cardP2 == 11):
        # player hits with ace in hand
        if ((pHTotal <= 17 and (cardD1 <= 3 or cardD1 >= 7)) or (pHTotal == 18 and (cardD1 >= 9))):
            hit = 0
            while((pHTotal <= 11) or (7 <= cardD1 and pHTotal <= 17 and hit == 0) or (pHTotal == 12 and (cardD1 == 2 or cardD1 == 3))):
                # print("player hits with ace in hand and total " + str(pHTotal) + " against dealer " + str(cardD1))
                # print("next card is " + str(stack[counter]))

                nextValue = stack[counter][0]
                if (nextValue == '1' or nextValue == 'J' or nextValue == 'Q' or nextValue == 'K'):
                    nextValue = 10
                elif (nextValue == 'A'):
                    if (pHTotal + 11 > 21):
                        nextValue = 1
                    elif (pHTotal + 11 <= 21):
                        nextValue = 11
                else:
                    nextValue = int(nextValue)
                pHTotal += nextValue
                if (pHTotal > 21):
                    pHTotal -= 10
                # print("new player total: " + str(pHTotal))
                counter += 1
                hit += 1
        # player stands with ace in hand
        elif (((pHTotal == 18) and (cardD1 == 2 or cardD1 == 7 or cardD1 == 8)) or (19 <= pHTotal <= 20)):
            if (pHTotal >= 19):
                # print("player stands with ace in hand automatically")    
                randomValue = 0
            else:
                # print("player stand with ace and 7 against dealer " + str(cardD1))
                randomValue = 0
        # player doubles with ace in hand
        elif ((13 <= pHTotal <= 18 and 4 <= cardD1 <= 6) or (pHTotal == 18 and cardD1 == 3)):
            # print("player doubles with ace in hand against dealer " + str(cardD1))
            # print("next card is " + str(stack[counter]))
            nextValue = stack[counter][0]
            if (nextValue == '1' or nextValue == 'J' or nextValue == 'Q' or nextValue == 'K'):
                nextValue = 10
            elif (nextValue == 'A'):
                if (pHTotal + 11 > 21):
                    nextValue = 1
                elif (pHTotal + 11 <= 21):
                    nextValue = 11
            else:
                nextValue = int(nextValue)
            pHTotal += nextValue
            if (pHTotal > 21):
                pHTotal -= 10
            # print("new player total: " + str(pHTotal))
            counter += 1
    
    # normal circumstances
    else:
        # player hits
        if ((pHTotal <= 8) or (pHTotal == 9 and (cardD1 == 2 or cardD1 >= 7)) or (pHTotal == 10 and cardD1 >= 10) or (pHTotal == 12 and (2 <= cardD1 <= 3 or cardD1 >= 7)) or (13 <= pHTotal <= 16 and cardD1 >= 7)):
            while((pHTotal <= 11) or (7 <= cardD1 and pHTotal < 17) or (pHTotal == 12 and (cardD1 == 2 or cardD1 == 3))):
                # print("player hits with " + str(pHTotal) + " against dealer " + str(cardD1))
                # print("next card is " + str(stack[counter]))

                nextValue = stack[counter][0]
                if (nextValue == '1' or nextValue == 'J' or nextValue == 'Q' or nextValue == 'K'):
                    nextValue = 10
                elif (nextValue == 'A'):
                    if (pHTotal + 11 > 21):
                        nextValue = 1
                    elif (pHTotal + 11 <= 21):
                        nextValue = 11
                else:
                    nextValue = int(nextValue)
                pHTotal += nextValue
                # print("new player total: " + str(pHTotal))
                counter += 1
        # player stands
        elif ((pHTotal >= 17) or (13 <= pHTotal <= 16 and cardD1 <= 6) or (pHTotal == 12 and 4 <= cardD1 <= 6)):
            # print("player stands with " + str(pHTotal) + " against dealer " + str(cardD1))
            randomValue = 0
        # player doubles
        elif((pHTotal == 9 and 3 <= cardD1 <= 6) or (pHTotal == 10 and 2 <= cardD1 <= 9) or (pHTotal == 11)):
            # print("player doubles bet with total " + str(pHTotal) + " against dealer " + str(cardD1))
            # print("next card is " + str(stack[counter]))
            nextValue = stack[counter][0]
            if (nextValue == '1' or nextValue == 'J' or nextValue == 'Q' or nextValue == 'K'):
                nextValue = 10
            elif (nextValue == 'A'):
                if (pHTotal + 11 > 21):
                    nextValue = 1
                elif (pHTotal + 11 <= 21):
                    nextValue = 11
            else:
                nextValue = int(nextValue)
            pHTotal += nextValue
            # print("new player total: " + str(pHTotal))
            counter += 1


    if (pHTotal > 21):
        # print("player se paso de verga")
        playerPassed += 1
    else:
        # dealer's turn
        # print('')
        # print("dealer reveals face-down card to be " + str(cardD2))
        # print("dealer has a total of " + str(dHTotal))
        while (dHTotal <= 16):
            # print("dealer takes another card with " + str(dHTotal))
            # print("next card is " + str(stack[counter]))
            nextValue = stack[counter][0]
            if (nextValue == '1' or nextValue == 'J' or nextValue == 'Q' or nextValue == 'K'):
                nextValue = 10
            elif (nextValue == 'A'):
                if (dHTotal + 11 > 21):
                    nextValue = 1
                elif (dHTotal + 11 <= 21):
                    nextValue = 11
            else:
                nextValue = int(nextValue)
            dHTotal += nextValue
            # print("new dealer total: " + str(dHTotal))
            if (dHTotal > 21):
                # print("dealer passed 21")
                dealerPassed += 1
            counter += 1        

    return [pHTotal, dHTotal, counter, bjClean, bjDirty, playerPassed, dealerPassed]