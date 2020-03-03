import sys

file_path = r"D:\python\orders.csv"

with open(file_path,"r") as file:
    for line in file:
        line = line.replace("\n","")
        order = line.split(",")

        try:

            pharmacy_name = order[0]
            item = order[1]
            amount = int(order[2])
            print('Order from drugstore "%s", item "%s", amount %d' %(pharmacy_name,item,amount))

        except ValueError as e:
            print("Problem with conversion to int in line %s" %(line),e)

        except IndexError as e:
            print("There are not enough columns in line %s" %(line),e)



        except:
            print("Problem with line %s" % line)
            print(sys.exc_info()[0])
        
        
        

print("Processing finished")
