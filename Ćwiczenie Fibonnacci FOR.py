##a1 = 0
##a2 = 1
##a3 = 0
##
##for i in range(1,21):
##    print('Step',i,'value',a3)
##    a1=a2
##    a2=a3
##    a3=a1+a2
##print(a3)


a1 = 0
a2 = 1
fib = 0

for i in range(1,21):
    print('Step',i,'value',fib)
    a1=a2
    a2=fib
    fib=a1+a2
    
    
