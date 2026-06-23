#Triangle pattern star

'''
for i in range(1,5):
    
    for j in range(1,i+1):
        
        print('*',end=' ')
    print() 

#Triangle pattern ascii character    

for i in range(1,6):
    
    for j in range(1,7-i):
        
        print(chr(96+j),end=' ')
        
    print() 

#Reverse triangle pattern star

for i in range(5,0,-1):
    
    for j in range(1,i+1):
        
        print('*',end=' ')
        
    print()
'''
#Mirror Triangle pattern star

n=int(input('Enter number of lines:'))

for i in range(n):
    for j in range(n):
        if j<n-i-1:
            print(' ',end=' ')
        else:
            print('*',end=' ')
    print()



