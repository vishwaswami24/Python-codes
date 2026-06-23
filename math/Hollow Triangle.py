#Hollow Triangle pattern


n=int(input('Enter Number:'))

for i in range(n):
    
    for j in range(n):
    
        if (i == j) or (j == 0) or (i == n-1):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

#Reverse hollow triangle

for i in range(n,0,-1):
    
    for j in range(n):
    
        if (i == j+1) or (j == 0) or (i == n):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()