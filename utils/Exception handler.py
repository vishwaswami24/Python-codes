try:
    x=int(input('Enter 1st value:'))
    y=int(input('Enter 2nd value:'))
    z=x/y
    print('Value:',z)
except ZeroDivisionError:
    print('Do not enter zero')

except ValueError:
    print('Enter integer')
