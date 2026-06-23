n=int(input('Enter number:'))      #4
i=1
f=1

while i<=n:
    f=f*i
    i=i+1
print('Factorial of',n,'is',f) 
'''
m=n
while m>0:              #  4>0 |  3>0  |   2>0  |  1>0 
    f=f*m               # 1*4=4| 4*3=12| 12*2=24| 24*1=24
    m=m-1               # 4-1=3| 3-1=2 | 2-1=1  |  1-1=0
print('Factorial of',n,'is',f) 
'''
