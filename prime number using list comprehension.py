#list comprehension
'''
value=int(input('Enter number:'))
prime=[x for x in range(2, value+1) if all(x % y != 0 for y in range(2, x))]
print(prime)
'''
min = 1

max = 100

primes = [num for num in range(min,max) if 0 not in [num%i for i in range(2,num//2)]]

print (primes)
