class grandparent:
    def get1(self):
        self.gname=input('Enter Grandpa name:')
        
class parent:
    def get2(self):
        self.pname=input('Enter father name:')
        
class child(grandparent,parent):
    def get3(self):
        self.cname=input('Enter name:')
    def display(self):
        print('My name is:',self.cname)
        print('My father name is:',self.pname)
        print('My grandfather name is:',self.gname)
c=child()
c.get1()
c.get2()
c.get3()
c.display()
