for x in range(1,6):
    line = str(x)
    for y in range(1,6):
        line += '\t' + str(x*y)
    print(line)
