colors = ['Hearts','Diamonds','Clubs','Spades']
figures = [{'Figure':'Ace',  'Power':14},{'Figure':'King', 'Power':13},
           {'Figure':'Queen','Power':12},{'Figure':'Jack', 'Power':11},
           {'Figure':'10',   'Power':10},{'Figure':'9',    'Power':9}]

allCards = []

for color in colors:
    for figure in figures:
        aCard = figure.copy()
        aCard['Color'] = color
        allCards.append(aCard)

import random

random.shuffle(allCards)
print(allCards, "\n")

player1 = []
player2 = []

seria = 1
for card in allCards:
    if seria % 2 == 0:
        player1.append(card)
    else:
        player2.append(card)
    seria+=1

print("player1 : ", player1, "\n")
print("player2 : ", player2, "\n")

while (len(player1) and len(player2)) != 0:
    card1 = player1.pop(0)
    card2 = player2.pop(0)

    if card1['Power'] == card2['Power']:
        player1.append(card1)
        player2.append(card2)
        print("Remis!: ", "Gracz 1: %d kart, Gracz 2: %d kart" %(len(player1),len(player2)))

    elif card1['Power'] > card2['Power']:
        player1.append(card1)
        player1.append(card2)
        print("Wygrał Player1: ", "Gracz 1: %d kart, Gracz 2: %d kart" %(len(player1),len(player2)))

    else:
        player2.append(card1)
        player2.append(card2)
        print("Wygrał Player2: ", "Gracz 1: %d kart, Gracz 2: %d kart" %(len(player1),len(player2)))


if len(player1)== 0:
    print( " Wygrał Gracz 2 ")
else:
    print( " Wygrał Gracz 1 ") 
    

    
        
    


    

       


        
