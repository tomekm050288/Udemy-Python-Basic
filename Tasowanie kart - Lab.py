colors = ['Hearts','Diamonds','Clubs','Spades']

figures = ['Ace','King','Queen','Jack','10','9']

allCards = []

for color in colors:
    for figure in figures:
        karta = color + " : " + figure
        allCards.append(karta)
print(allCards, "\n")

import random

random.shuffle(allCards)

print(allCards, '\n')

player1 = []
player2 = []

max = len(allCards)

for i in range(0,max-1):
    if i % 2 == 0:
        player1.append(allCards[i])
    else:
        player2.append(allCards[i])
print('1 gracz: ',player1,'\n','2 gracz: ', player2, '\n')

player3 = []
player4 = []

player3 = allCards[0:11]
player4 = allCards[12:]

print('3 gracz: ',player3,'\n','4 gracz: ', player4, '\n')





