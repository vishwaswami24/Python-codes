class parent:
    def getp(self):
        self.p=input('Enter name:')
class child1(parent):
    def getc1(self):
        self.c1=input('Enter child1 name:')
    def display(self):
        print('Child1 name is:',self.c1)
        print('Parent name is:',self.p)
class child2(parent):
    def getc2(self):
        self.c2=input('Enter child1 name:')
    def display(self):
        print('Child1 name is:',self.c2)
        print('Parent name is:',self.p)
c1=child1()
c1.getp()
c1.getc1()
c1.display()
c2=child2()
c2.getp()
c2.getc1()
c2.display()
