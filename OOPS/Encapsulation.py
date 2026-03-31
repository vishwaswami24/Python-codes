'''
# public class data members

class customer:
    def getdata(self):
        print('getdata called')
        self.name=input('Enter name:')
        self.add=input('Enter location:')
        self.display()            #calling display in class
    def display(self):
        print('display called')
        print('NAME:',self.name)
        print('LOCATION:',self.add)
        
c=customer()
c.getdata()
print('Name-',c.name)
'''
#private class data members

class customer:
    def getdata(self):
        print('getdata called')
        self.name=input('Enter name:')
        self.__add=input('Enter location:')    #private data member
        self.__display()                       #calling private method display in class 
    def __display(self):                       #private method                  
        print('display called')
        print('NAME:',self.name)
        print('LOCATION:',self.__add)
        
c=customer()
c.getdata()
print('Address-',c.getdata.__add)         #publically retriving private variable