#multi-level inheritance
class grandparent:
    def get1(self):
        self.gname=input('Enter Grandpa name:')
        
class parent(grandparent):
    def get2(self):
        self.pname=input('Enter father name:')
        
class child(parent):
    def get3(self):
        self.cname=input('Enter name:')
    def display(self):
        print('\nMy name is '+self.cname + self.pname +' Swami')
        print('My father name is '+ self.pname +self.gname +' Swami')
    
c=child()
c.get1()
c.get2()
c.get3()
c.display()
