countries = ['Uruguay','Russia','Saudi Arabia','Egypt','Spain','Portugal','Iran',
             'Morocco','France','Denmark','Peru','Australia','Croatia',
             'Argentina','Nigeria','Iceland','Brazil','Switzerland','Serbia',
             'Costa Rica','Sweden','Mexico','Korea Republic','Germany',
             'Belgium','England','Tunisia','Panama','Colombia','Japan','Senegal',
             'Poland']

import random

random.shuffle(countries)
counter = 0
print("Zaczynamy losowanie!")  
for country in countries:
    if countries.index(country) % 4 == 0:
        counter +=1
        print("-------------GRUPA %s ------------- " % (counter))
    print(country)
        
        
      
      
    
