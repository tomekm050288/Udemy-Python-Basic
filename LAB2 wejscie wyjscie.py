import os


while True:
    filename = input("Enter filepath: ")
    if os.path.isfile(filename):
        break
    else:
        print("Enter filepath ones again!")

webaddresses = []

with open(filename,"r") as file:
    for line in file:
        new_line = line.replace("\n","")
        webaddresses.append(new_line)


for item in webaddresses:
    if item.endswith(".pl"):
        print("adres %s jest adresem z Polski" %(item))
    else:
        print("adres %s nie jest adresem z Polski" %(item))
