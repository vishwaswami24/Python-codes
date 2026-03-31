class gparent:
    def display(self):
        print('Grandparent class')
class son(gparent):
    def display_s(self):
        print('Son class')
class d_in_law(gparent):
    def display_d(self):
        print('Daughter-in-law class')        
class child(son,d_in_law):
    def display_c(self):
        print('Child class')
        
c=child()
c.display()
c.display_s()
c.display_d()
c.display_c()
