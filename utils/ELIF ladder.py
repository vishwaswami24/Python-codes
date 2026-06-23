x=int(input('Enter 1st value:'))
y=int(input('Enter 2nd value:'))
z=int(input('Enter 3rd value:'))

if x>y and x>z:
    print(x,'is greater')
elif y>x and y>z:
    print(y,'is greater')
else: 
    print(z,'is greater')

