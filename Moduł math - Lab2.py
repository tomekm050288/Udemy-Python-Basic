degree = 45
import math

stopien = math.pi/180

#print(stopien*degree)

#print(math.radians(180),math.radians(45))

small_pizza_r = 22
big_pizza_r = 27
family_pizza_r = 38
small_pizza_price = 11.50
big_pizza_price = 15.60
family_pizza_price = 22.00

pizze = ['small_pizza_r','big_pizza_r', 'family_pizza_r']
rozmiar = [22,27,38]
ceny = [11.50,15.60,22.00]
cenazametr = []

for i in range(len(pizze)):
    print(math.pi*rozmiar[i]**2)
    print(ceny[i]/(math.pi*(rozmiar[i]/100)**2))
    
math_ls = dir(math) 
print(math_ls)
