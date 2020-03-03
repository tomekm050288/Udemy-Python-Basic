import os
import time

dir = input("Insert path: ")
print("This filepath is :%s" %(dir))

while not os.path.isdir(dir):
    print("This is not directory")
    break
else:
    file = input("Insert filename: ")
    path = os.path.join(dir,file)
    print("Path: ", path)
    if not os.path.exists(path):
        print("Path don\'t exists!")
    else:
        print("File properties: \n")
        print("Last modification: ", time.localtime(os.path.getmtime(path)),'\n')
        print("Size in bytes: ", os.path.getsize(path),'\n')
        print("Folder information: ",os.getcwd(),'\n')
        print("Relative path: ", os.path.relpath(path),'\n')

    
