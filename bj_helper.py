# program so you can put your hand and dealer card 
# and it gives you the ideal strategy according to 
# the BOOK
from utils.theBookPersonal import theBook
from utils.theBookPersonal import theBook2

def startingHand():
    hand = input("What are you card values? ")
    arr_hand = hand.split(" ")
    cardP1 = int(arr_hand[0])
    cardP2 = int(arr_hand[1])
    dealer = int(input("What does the dealer have? "))
    theBook(cardP1, cardP2, dealer)
    return dealer

def main():
    for i in range(100):
        dealer = startingHand()

        continue_round = input("Continue? (y/n): ")
        while(continue_round == 'y'):
            if (continue_round == 'y'):
                newTotal = int(input("What is your new total? "))
                theBook2(newTotal, dealer)
            continue_round = input("Continue? (y/n): ")

if __name__ == "__main__":
    main()
