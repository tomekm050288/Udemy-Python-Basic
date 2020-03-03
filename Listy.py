hitsTitles = ['BROTHERS IN ARMS','BOHEMIAN RHAPSODY',\
              'STAIRWAY TO HEAVEN','RIDERS ON THE STORM',\
              'WISH YOU WERE HERE']
hitsTitles.append('CHILD IN TIME')
hitsTitles.append('AGAIN')
hitsTitles.insert(3,'HOTEL CALIFORNIA')
#print(hitsTitles)
hitsTitles.insert(0,'THE SOUND OF SILENCE')
#print(hitsTitles.index('HOTEL CALIFORNIA'))
#print(hitsTitles)
hitsTitles.remove('HOTEL CALIFORNIA')
hitsTitles[0] = "ENJOY THE SILENCE"
print(hitsTitles)
hitsToRead = hitsTitles.copy()
hitsToRead.reverse()

print(hitsToRead)

hitsToRead.sort()

print(hitsToRead)

print(hitsToRead.pop(0))
print(hitsToRead)

print(hitsToRead.pop(0))
print(hitsToRead)

additionalSongs = ['NOTHING COMPARES 2 U','WISH YOU WERE HERE']
hitsToRead.extend(additionalSongs)

print(hitsToRead)

print('WISH YOU WERE HERE: ', hitsToRead.count('WISH YOU WERE HERE'),'\n',
      'RIDERS ON THE STORM: ', hitsToRead.count('RIDERS ON THE STORM'))

hitsToRead.clear()
print(hitsToRead)

