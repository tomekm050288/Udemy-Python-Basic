silnia = 1

for x in range(1,11):
    silnia *= x
    print(x, "!:" , silnia)

x = 10



for i in range(1,x+1):
    silnia = 1
    for j in range(1,i+1):
        silnia = silnia*j
    print(i,'!= ', silnia, sep = '')
        
