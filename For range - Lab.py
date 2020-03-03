string_A = '+---+---+---+---+'
string_B = '|   |   |   |   |'

##for i in range(10):
##    print(string_A

for i in range(5):
  print(string_A)
  print(string_B)

i=1
for i in range(10):
    print('x'*i)
    i+=1
    
i=1
for i in range(1,9,2):
    print('o'*i)
    print('x'*(i+1))


for i in range(1,10):
    if i % 2 == 0:
        print("x"*i)
    else:
        print("o"*i)


for i in range(9):
    if i % 2 == 0:
        print(string_A)
    else:
        print(string_B)
    
