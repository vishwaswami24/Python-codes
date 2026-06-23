
class A:                                    #base class
    def get1(self):
        self.a=int(input('Enter value:'))
    def disp1(self):
        print('Value of A is:',self.a)
class B(A):                                 #derived class
    def get2(self):
        self.b=int(input('Enter value:'))
    def display(self):
        print('Value of B is:',self.b)
        print('Value of A is:',self.a)
        
b=B()                        #class B object
b.get1()                     #derived method from parent class A
b.get2()
b.display()
b.disp1()                    #derived method from parent class A
b.a()
