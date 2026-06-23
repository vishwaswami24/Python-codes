#Swap two numbers using 3 variables

a=int(input('Enter 1st value:'))        #a=10
b=int(input('Enter 2nd value:'))        #b=20

temp=a
a=b                                     #a=20
b=temp                                  #b=10

print('After Swapping')

print('1st value:',a)
print('2nd value:',b)

#Swap two numbers using 2 variables
#method 1
a,b=b,a                                 #a=10,b=20

print('After Swapping')

print('1st value:',a)
print('2nd value:',b)

#method 2
a=a+b                                   #a=30
b=a-b                                   #b=10
a=a-b                                   #a=20

print('After Swapping')

print('1st value:',a)
print('2nd value:',b)

#method 3
a=a*b                                  #a=200
b=a//b                                 #b=20
a=a//b                                 #a=10

print('After Swapping')

print('1st value:',a)
print('2nd value:',b)
