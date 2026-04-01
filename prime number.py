#prime number

n=int(input('Enter number:'))

for i in range(2,n,1):
    r=n%i
    if r==0:
        print('Not Prime')
        break
else:
        print('Prime')
