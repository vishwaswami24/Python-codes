class marks:
    def getdata(self):
        self.a=int(input('Enter value:'))
    def __add__(self,other):
        print('Inside add method')
        t=marks()
        t.a=m1.a+m2.a
        return t
    def display(self):
        print('Value is:',self.a)
        
m1=marks()
m2=marks()
m3=marks()
m1.getdata()
m2.getdata()
m3=m1+m2
m3.display()

        
