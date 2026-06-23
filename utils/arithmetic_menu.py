print('''OPTIONS
        1.Addition
        2.Subtraction
        3.Multiplication
        4.Division\n''')

a=int(input('Enter 1st number:'))
b=int(input('Enter 2nd number:'))
x=int(input('OPTION:'))

if x==1:
    print('Addition:',a+b)
elif x==2:
    print('Subtration:',a-b)
elif x==3:
    print('Multiplication:',a*b)
elif x==4:
    print('Division:',a//b)
else:
    print('Enter valid choice')
