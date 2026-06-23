class gparent:
    def getdata(self):
        self.gname=input('Enter grandparent name:')

class parent(gparent):
    def getdata(self):
        self.pname=input('Enter parent name:')
        super().getdata()
    def display(self):
        print('Parent name is:',self.pname)
        print('Grandparent name is:',self.gname)
p=parent()
p.getdata()
p.display()

        
