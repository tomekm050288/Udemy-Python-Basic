file_path = r"D:\python\orders.csv"

with open(file_path,"r") as file:
    for line in file:
        line = line.replace("\n","")
        order = line.split(",")
        if len(order) == 3:
            print('Order from drugstore "%s", item "%s"' %(order[0],order[1]))
        else:
            print("Line %s malformed!!!" %(line))
        print(line)

print("Processing finished")
