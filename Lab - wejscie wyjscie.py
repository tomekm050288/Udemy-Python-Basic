import os

webaddresses = []

line = input("Enter www address :")

while line:
    webaddresses.append(line)
    line = input("Enter www address :")

dirname = os.getcwd()

filename = input("Enter filename: ")
filepath = os.path.join(dirname,filename)

with open(filepath,"w") as file:
    for address in webaddresses:
        file.write(address + "\n")
    
