text = '''Industrial Light & Magic: In this case, you find Python
    used in the production process for scripting complex,
    computer graphic-intensive films. Originally, Industrial
    Light & Magic relied on Unix shell scripting, but it was
    found that this solution just couldn’t do the job. Python
    was compared to other languages, such as Tcl and Perl, and
    chosen because it’s an easier-to-learn language that the
    organization can implement incrementally. In addition, Python
    can be embedded within a larger software system as a scripting
    language, even if the system is written in a language such as
    C/C++. It turns out that Python can successfully interact with
    these other languages in situations in which some languages can’t.'''

text_list = text.replace('\n',' ').split(" ")

for item in text_list:
    if 'p' in item:
        print(item)


dictionary={'A':'80%-100%','B':'60%-80%','C':'50-60%','D':'less then 50%'}

for key,value in dictionary.items():
    print(key," - ",value)



text_list = text.replace('\n',' ').split(" ")

newDict = {}

for word in text_list:
    if word in newDict.keys():
        continue
    newDict[word] = text_list.count(word)
print(newDict)

##wordDictionary={}
##for word in text_list:
##    if word in wordDictionary.keys():
##        wordDictionary[word] = wordDictionary[word]+1
##    else:
##        wordDictionary.setdefault(word,1)
##        
##print(wordDictionary)
