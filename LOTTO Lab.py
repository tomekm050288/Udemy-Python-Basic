import random

wylosowane = []

while len(wylosowane) < 7:
    number = random.randint(1,49)
    if number in wylosowane:
        print("Eiminated")
        continue
    wylosowane.append(number)
print(wylosowane)
