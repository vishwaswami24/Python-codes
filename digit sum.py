#Digit sum

n=123

a=n%10

n=n//10

b=n%10

n=n//10

c=n%10

d=a+b+c

print('Digit sum:',d)

m=int(input())
q=0

while m>0:
    p=m%10
    q=q+p
    m=m//10
print(q)   

