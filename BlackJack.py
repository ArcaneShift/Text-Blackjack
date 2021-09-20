import random

deck = []
pHand = []
dHand = []
pTotal=0
dTotal=0
score=0

def shuffleDeck():
    for i in pHand:
        deck.append(i)
    for i in dHand:
        deck.append(i)
       
    random.shuffle(deck)

def dtapCard():
    dHand.append(deck[0])
    deck.pop(0)
    a = dHand[-1]
    print("Deler drew a",a[1], "of", a[0])
   

def ptapCard():
    pHand.append(deck[0])
    deck.pop(0)
    a = pHand[-1]
    print("You drew a",a[1], "of", a[0])
    

def calculateHand(hand):
    total=0
    choices = {'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11 , 2: 2, 3: 3,4: 4,5: 5,6: 6,7: 7,8: 8,9: 9,10: 10}
    
    for i in hand:
        result=choices.get(i[1], 'default')
        total+=result
        #print(result)

    for i in deck:
        if(total >21 and i == 'Ace'):
            total-=10
        elif(total<22):
            break

    #print()
    #print("Your hands total is:",total)
    return total

def displayHand():
    print("Your hand is: ")
    for i in pHand:
        print(i[1], "of",i[0])
       
    

    print()
    a = dHand[0]
    print("Dealer is showing a",a[1], "of", a[0])
    
def dealerReveal():
    print("The dealers hand is: ")
    for i in dHand:
        print(i[1], "of",i[0])

def dealHand():
    pHand.append(deck[0])
    deck.pop(0)
    pHand.append(deck[0])
    deck.pop(0)

    dHand.append(deck[0])
    deck.pop(0)
    dHand.append(deck[0])
    deck.pop(0)

def makeDeck():
    suite = "Clubs"
    for i in range(12):
    
        if(i>1 and i<11):
            tuple = (suite,i)
            deck.append(tuple)
        elif(i==1):
            tuple = (suite,"Ace")
            deck.append(tuple)
        elif(i>10):
            tuple = (suite, "Jack")
            deck.append(tuple)
            tuple = (suite, "Queen")
            deck.append(tuple)
            tuple = (suite, "King")
            deck.append(tuple)

    suite = "Spades"        

    for i in range(12):
    
        if(i>1 and i<11):
            tuple = (suite,i)
            deck.append(tuple)
        elif(i==1):
            tuple = (suite,"Ace")
            deck.append(tuple)
        elif(i>10):
            tuple = (suite, "Jack")
            deck.append(tuple)
            tuple = (suite, "Queen")
            deck.append(tuple)
            tuple = (suite, "King")
            deck.append(tuple)
            
    suite = "Hearts"        

    for i in range(12):
    
        if(i>1 and i<11):
            tuple = (suite,i)
            deck.append(tuple)
        elif(i==1):
            tuple = (suite,"Ace")
            deck.append(tuple)
        elif(i>10):
            tuple = (suite, "Jack")
            deck.append(tuple)
            tuple = (suite, "Queen")
            deck.append(tuple)
            tuple = (suite, "King")
            deck.append(tuple)
            
    suite = "Diamonds"        

    for i in range(12):
    
        if(i>1 and i<11):
            tuple = (suite,i)
            deck.append(tuple)
        elif(i==1):
            tuple = (suite,"Ace")
            deck.append(tuple)
        elif(i>10):
            tuple = (suite, "Jack")
            deck.append(tuple)
            tuple = (suite, "Queen")
            deck.append(tuple)
            tuple = (suite, "King")
            deck.append(tuple)
            

   # print(deck)
   # print("\n")
    shuffleDeck()
    #print(deck)

def main():
    makeDeck()
    #print(deck)
   # print(*deck, sep='\n')

    
  #  print("\n")
   # print(*pHand, sep='\n')
    #print(*dHand, sep='\n')
    #shuffleDeck()
    #print
    while(1):
        dealHand()
        displayHand()

        print("Would you like to hit?")
        while(1):
            userInput = input()

            if(userInput == "Yes" or userInput == "yes" or userInput == "y" or userInput == "Y"):
                ptapCard()
                print("Would you like to hit again?")
            elif(userInput == "No" or userInput == "no" or userInput == "n" or userInput == "N"):
                break

        dealerReveal()
        while(1):
            if(calculateHand(dHand) < calculateHand(pHand) and calculateHand(dHand) > 16 and calculateHand(pHand) > 21):
                break
            elif(calculateHand(dHand) < calculateHand(pHand)):
                dtapCard()
            else:
                break
        dTotal = calculateHand(dHand)
        pTotal = calculateHand(pHand)
        print("Dealers total is:",dTotal,"and your total is:", pTotal)
        if(dTotal > pTotal and dTotal < 22):
            print("The dealer won")
        elif(dTotal > 21 and pTotal < 22):
            print("You won!")
        elif(dTotal > 21 and pTotal > 21):
            print("You both went over")
        else:
            print("It's a tie")

        print("Would you like to play again?")
        userInput = input()
      
            
        if(userInput == "No" or userInput == "no" or userInput == "n" or userInput == "N"):
            break
           
        shuffleDeck() 



if __name__ == "__main__":
    main()
