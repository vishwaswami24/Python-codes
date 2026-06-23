'''
#summation of all data in list

data=input('Enter values:')
print(type(data))

sum=0
lst=data.split()

for i in lst:
    sum=sum+int(i)
print(sum)    
'''
'''
#Max valuue in the list

l=[10,20,-2,50,40,3]
max=l[0]

for i in l:
    if i>max:
        max=i
print(max)        
'''

#seperate +ve and -ve numbers in 2 different lists

l=[10,20,-30,-89,0,75,-99]
print(l)
pl=[]
nl=[]

for i in l:
    if i!=0:
        if i>0:
            pl.append(i)
        else:
            nl.append(i)
print(pl)
print(nl)
