import math

a_str = input("Podaj a: ")
b_str = input("Podaj b: ")
c_str = input("Podaj c: ")

def check_int(s):
    if s[0] in ('-', '+'):
        return s[1:].isdigit()
    return s.isdigit()

while not (check_int(a_str) and check_int(b_str) and check_int(c_str)):
    print("Jedna z liczba a,b,c nie jest całkowita!!!")
    break
else:
    a = int(a_str)
    b = int(b_str)
    c = int(c_str)
    if a == 0:
        print("To nie jest równanie kwadratowe!!!")
    else:
        delta = b**2 - 4*a*c
        if delta < 0:
            print("Brak rozwiązań!!")
        elif delta == 0:
            x1 = -b/(2*a)
            print("Jedno miejsce zerowe x1 = ", x1)
        else:
            x1 = (- b - math.sqrt(delta))/(2*a)
            x2 = (- b + math.sqrt(delta))/(2*a)
            print("Dwa miejsca zerowe x1 = ", x1, "x2 = ",x2)

        
