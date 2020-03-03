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

dirname = os.path.dirname(filename)

for item in webaddresses:
    if item.endswith(".pl"):
        path_name = os.path.join(dirname,'webs_pl.txt')
        with open(path_name, "a") as file:
            file.write(item + "\n")
    else:
        path_name = os.path.join(dirname,'webs_other.txt')
        with open(path_name, "a") as file:
            file.write(item + "\n")
