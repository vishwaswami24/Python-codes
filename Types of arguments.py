
def add(a,b):
    c=a+b
    print(c)
add(10)    #returns positional argument missing

# Default Argument

def add(a,b=10):
    c=a+b
    print(c)
add(10)  
add(10,50)      #default value changed

# Keyword Argument

def sub(x,y):
    z=x-y
    print(z)
sub(x=50,y=20)

# Variable length argument

  #Non-key word arguments using *
  
def display(*x):
   print(type(x))
   print(x)
display(10,20,30)
display(1,9,-5,-7)

   #Keyword arguments using **

def display(**x):
    print(type(x))
    print(x)
display(x=10,y=20)


   
