'''
class constructor:                          #default constructor
    def __init__(self):
     
        print('Inside the function')

s=constructor()
'''
class customer():
    def __init__(self):
        self.bname='SBI'
        self.ifsc='SBIN0020363'
        self.loc='LATUR'
    def getdata(self):
        self.name=input('Enter name:')
        self.num=input('Enter mobile number:')
        self.acc=input('Enter account number:')
        print()
    def display(self):
        print('Bank Name:',self.bname)
        print('IFSC code:',self.ifsc)
        print('Bank Location:',self.loc)
        print()
        print('----------------------------------')
        print('Customer name:',self.name)
        print('Customer mobile number',self.num)
        print('Customer account number',self.acc)
        
c=customer()
c.getdata()
c.display()
