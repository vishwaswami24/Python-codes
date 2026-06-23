classname='itvedant'      #global variable
def display():
    classname='it_vedant' #local scope prioritize local variable 
    print(classname)
    branch='pune'         #local variable 
    print(branch)
display()    

print(classname)
