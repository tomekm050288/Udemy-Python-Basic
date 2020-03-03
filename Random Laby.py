import random

##print(random.randint(1,100))
##
##for i in range(10):
##    print(random.randint(1,100))

number1 = random.randint(1,100)
print(number1)
counter = 1
number2 = 0

while number2 != number1:
    number2 = random.randint(1,100)
    print(number2, counter)
    counter += 1
    if number2 == number1:
        print('Udało się! ', 'number1: ',number1, ' = ','number2: ',number2)
    
