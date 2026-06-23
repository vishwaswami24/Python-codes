#Armstrong Number

n=int(input('Enter number:'))
a=n%10
b=n//10
c=b%10
d=b//10

num=a**3+c**3+d**3

if n==num:
    print('Armstrong Number')
else:
    print('Not Armstrong Number')
    
