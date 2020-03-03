import os
import sys

##line = input("What is acceptable price of course on Udemy? ")
##
##filepath = input("Enter filepath: ")
##
##with open(filepath, "w+") as file:
##    file.write(line)


try:
    line = input("What is acceptable price of course on Udemy? ")
    filepath = input("Enter filepath: ")
    
    with open(filepath, "w+") as file:
        file.write(line)

    value = int(line)
    print("The value saved in file is %d" %(value))

          
except FileNotFoundError as e:
    print("Error opening file", e)
    print(sys.exc_info()[0])

except ValueError as e:
    print("The value entered cannot be converted to a number", e)
    print(sys.exc_info()[0])
    
except:
    print("SORRY - WE HAVE AN ERROR")

else:
    print("Actions completed successfully")
