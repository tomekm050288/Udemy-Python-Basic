import random
dices = []
min = 1
max = 6

for i in range(5):
    dices.append(random.randint(min,max))
dices.sort()
print(dices)
