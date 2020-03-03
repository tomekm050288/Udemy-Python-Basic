text = '''
United Space Alliance: This company provides major support to NASA for
various projects, such as the space shuttle. One of its projects is to
create Workflow Automation System (WAS), an application designed to
manage NASA and other third-party projects. The setup uses a central
Oracle database as a repository for information. Python was chosen over
languages such as Java and C++ because it provides dynamic typing and
pseudo-code–like syntax and it has an interpreter. The result is that
the application is developed faster, and unit testing each piece is easier.
'''
wordLength = 6

listOfWords = text.replace('\n',' ').split(" ")
shortWords = 0
longWords = 0

for item in listOfWords:
    if len(item) > wordLength:
        longWords += 1
    else:
        shortWords += 1
print(longWords, shortWords)
    
        
        
text = '''
United Space Alliance: This company provides major support to NASA for
various projects, such as the space shuttle. One of its projects is to
create Workflow Automation System (WAS), an application designed to
manage NASA and other third-party projects. The setup uses a central
Oracle database as a repository for information. Python was chosen over
languages such as Java and C++ because it provides dynamic typing and
pseudo-code–like syntax and it has an interpreter. The result is that
the application is developed faster, and unit testing each piece is easier.
'''
listOfWords = text.replace('\n',' ').split(' ')
wordLength = 6
i=0
shortWords = 0
longWords = 0
while i< len(listOfWords):
    if len(listOfWords[i])>wordLength:
        longWords+=1
    else:
        shortWords+=1
    
    i+=1
print("Words shorter than ",wordLength,":",shortWords)
print("Words longer than ",wordLength,":",longWords)

