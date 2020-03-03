import math
import geom



def GiveGeomSeqElement(a1=2,factor=2,index=2):
    #returns n-th term of geometric sequence starting with element a1 and having 
    value = a1*pow(factor,index-1)# a1 * factor**index-1 - wzór na ciąg
    return value
print('2^64 =',GiveGeomSeqElement(1,2,64))
print('------------------------------------------------')

counter = 1
a1 = 3
factor = 2
maxindex = 10
print("a1 = ", a1)
for element in range(maxindex - 1):
    counter += 1
    print('a%d = ' %(counter),GiveGeomSeqElement(a1,factor,counter), '\n')


##a1=3
##factor=2
##maxindex=10
##for i in range(1,maxindex):
##    an = GiveGeomSeqElement(a1=a1,factor=factor,index=i)
##    print('Term ',i,'=',an)
##print('------------------------------------------------')




def GiveFactorForGeomSeq(a1,a_next):
    factor = a_next / a1
    return factor

print('factor = ', GiveFactorForGeomSeq(12,24))






def GiveSumOfNElementsGeomSeq(a1 = 2, factor = 2,index = 2):

    ciag_geom = []
    ciag_geom.append(a1)
    for i in range(index-1):
        a2 = a1*factor
        ciag_geom.append(a2)
        a1 = a2

    return sum(ciag_geom)
    

print("Suma ciągu: ", GiveSumOfNElementsGeomSeq(2,3,4))



def GiveSumOfNElementsGeomSeq2(a1 = 2, factor = 2,index = 2):

    suma = a1*(1-pow(factor,index))/(1-factor)
    return suma

print("Suma ciągu: ", GiveSumOfNElementsGeomSeq2(2,3,4))
    


import geom

print('2^64 =',geom.GiveGeomSeqElement(1,2,64))
print('------------------------------------------------')
a1=3
factor=2
maxindex=11
for i in range(1,maxindex+1):
    an = geom.GiveGeomSeqElement(a1=a1,factor=factor,index=i)
    print('Term ',i,'=',an)
print('------------------------------------------------')
print('Factor is', geom.GiveFactorForGeomSeq(12,24))
print('------------------------------------------------')
print('Sum of n elements is', geom.GiveSumOfNElementsGeomSeq(2,3,4))
        
