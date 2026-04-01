'''
def display():
    print('FK')
    display()

display()    


#summation from 1 to 5 by recursion

n=int(input('Enter number:'))
def sum(n):
    if n==1:
        return 1
    s=n+sum(n-1)
    return s
t=sum(n)
print(t)

'''

#factorial of given number using recursion

n=int(input('Enter number:'))
def fact(n):
    if n==1:
        return 1
    f=n*fact(n-1)
    return f

t=fact(n)
print(t)

#fibonacci series

n=int(input('Enter number:'))

def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1)+ fib(n-2)

if n <= 0:
    print("Enter positive number.")
else:
    for i in range(n): 
        print(fib(i))
