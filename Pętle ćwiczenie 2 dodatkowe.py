##number = 20730906
##number_str = str(number)
##new_list = []
##
##for item in number_str:
##    new_list.append(int(item))
##    suma = 0
##    for cyfra in new_list:
##        suma +=cyfra
##print(suma)
    
    
number=20730906
tmpnumber = number
sumOfDigits = 0
while tmpnumber >0:
    digit = tmpnumber % 10
    sumOfDigits += digit
    tmpnumber = tmpnumber//10
else:
    print('the sum of digits of ', number, ' is',sumOfDigits)
