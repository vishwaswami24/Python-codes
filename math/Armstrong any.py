
num=int(input('Enter Number:'))
order=len(str(num))
sum=0
n=num
while n>0:
        x=n%10
        sum+=x**order
        n=n//10
if num==sum:
        print('Armstrong')
else:
        print('No')
