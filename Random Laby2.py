countries = ['Uruguay','Russia','Saudi Arabia','Egypt','Spain','Portugal','Iran','Morocco','France','Denmark','Peru','Australia','Croatia','Argentina','Nigeria','Iceland','Brazil','Switzerland','Serbia','Costa Rica','Sweden','Mexico','Korea Republic','Germany','Belgium','England','Tunisia','Panama','Colombia','Japan','Senegal','Poland']

import random
##random.shuffle(countries)
##print(countries)
##groupNumber = 1
##
##
##while groupNumber <= len(countries):
##    random_country = random.choice(countries)
##    print(random_country, ":",groupNumber)
##    if countries.index(random_country) % 4 == 0:
##        groupNumber += 1
##        print("Grupa: ",groupNumber)


random.shuffle(countries)
 
groupNumber = 0
 
for i in range(len(countries)):
    if i % 4 == 0:
        groupNumber += 1
        print("========== Group %d ==========" % (groupNumber))
    print(countries[i])






    
