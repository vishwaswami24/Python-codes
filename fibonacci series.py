#fibonacci series

n=int(input('Enter number:'))
i=0
j=1
k=1
print(i,end=' ')
print(j,end=' ')
while k<=n-2:
    sum=i+j
    print(sum,end=' ')
    i=j
    j=sum
    k+=1
