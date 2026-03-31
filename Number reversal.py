n=int(input('Enter the number:'))
sum=0

while n>0:
    x=n%10
    
    sum=sum*10+x
    
    n=n//10
    
print(sum) 
