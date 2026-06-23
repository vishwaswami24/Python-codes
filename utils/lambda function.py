'''
t=lambda a,b,c:a+b+c
s=t(10,20,30)
print(s)

t=lambda x:x>0
print(t(5))
'''

#filter function

l=[10,20,30,-50,-60,-70]
t=list(filter(lambda i:i>0,l))
print(t)

    #Even-Odd

lt=[1,2,3,4,5,6]

e=list(filter(lambda i:i%2==0,lt))
print(e)

o=list(filter(lambda i:i%2!=0,lt))
print(o)

#map function

sq=list(map(lambda i:i*i,lt))
print(sq)

