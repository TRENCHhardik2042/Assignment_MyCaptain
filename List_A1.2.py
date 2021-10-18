L1 = ['a' , 2 , 'c' , 4 ,7 ,5 , 4]
print(L1)

#appending 
L1.append('free')
print(L1)

#counting 
y = L1.count(4)
print(y)


#clearing
L1.clear() 
print(L1)

#copy a list 
L2 = [1, 2, 3, 4]
L1 = L2.copy()
print(L1)
print(L2)

#extend
L2.append('free')

L1.extend(L2)
print(L1)


#indexing

z = L1.index('free')
print(z)

#inserting 

L2.insert(1 ,'free')
print(L2)

#pop
L2.pop(1)
print(L2)

#remove

L2.remove('free')
print(L2)

#reverse 
L1.reverse()
print(L1)

#sorting 

L3 = ['Apple' ,'Banana','Orange','Mango', 'Chicko', 'Blueberry' ]
L3.sort()
print(L3)




