initialCapital = 20000
percent = 0.03
maxTimeYears = 10

account = initialCapital

##for i in range(1,maxTimeYears+1):
##    account += account*percent
##    print(account,i)

i = 1
while i <=10:
    account += account*percent
    print(round(account,2),i)
    i+=1
else:
    print('the total revenue is', round(account-initialCapital,2))

year=0
capital=initialCapital
while year<maxTimeYears:
    year+=1
    capital=round((1+percent)*capital,2)
    print('after this year:', year,  'you will have:',capital)
else:
    print('the total revenue is', capital-initialCapital)
