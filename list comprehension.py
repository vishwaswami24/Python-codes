#list comprehension
'''
l=[1,2,3,4,5]
l1=[]

l1=[2*i for i in l]
print(l1)
'''
'''
n={i:2*i for i in range(1,5)}
print(n)

'''

n=int(input('Enter number:'))

l=list(map(lambda i:n%i,range(n)))
