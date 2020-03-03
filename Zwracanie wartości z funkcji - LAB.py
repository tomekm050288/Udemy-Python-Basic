def PrintAnimal(*animals):
    txt_cat = r'''
|\---/|
| o_o |
 \_^_/'''


    txt_bear = r'''
/  \.-"""-./  \
\    -   -    /
 |   o   o   |
 \  .-'"'-.  /
  '-\__Y__/-'
     `---`'''

    txt_bat = r'''
   /\                 /\
  / \'._   (\_/)   _.'/ \
 /_.''._'--('.')--'_.''._\
 | \_ / `;=/ " \=;` \ _/ |
  \/ `\__|`\___/`|__/`  \/
          \(/|\)/  
     '''
    for animal in animals:
        if animal == "bat":
            print(txt_bat)
        elif animal == "cat":
            print(txt_cat)
        elif animal == 'bear':
            print(txt_bear)
        else:
            print("Cannot print '%s'. Correct values for the parameter are: cat, bear, bat" %(animal))
    return
        
   

        

PrintAnimal('bat','cat','bear','dog','coś')






