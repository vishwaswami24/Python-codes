#Palindrome

n=int(input('Enter number:'))
a=n%10
b=n//10
c=b%10
d=b//10

rev=a*100+c*10+d*1

if n==rev:
    print('Palindrome number')
else:
    print('Not Palindrome Number')
