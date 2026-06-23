from datetime import date

class library:
    acc_number=input("Account number:")
    publisher=input("Book Publisher:")
    title=input("Book Title:")
    author=input("Book Author:")

    d1=input("Date of Issue(YYYY-MM-DD):").split('-')
    y,m,d= [int(i) for i in d1]
    doi=date(y,m,d)

    d2=int(input("Number of days issued:"))

    d3=input("Date of Return(YYYY-MM-DD):").split('-')
    y,m,d= [int(i) for i in d3]
    dor=date(y,m,d)

    ltd = dor-doi
    d4 = ltd.days
    f = d4*1.5
    
    def read(self):
        print()
        print(" CENTRAL-LIBRARY ".center(70,'-'))
        print("Library Card".center(70))
        print()
        print(" Account number:",self.acc_number)
        print(" Book Title:",self.title)
        print(" Book Author:",self.author)
        print()

    def calculate(self):
        print(" Date of Issue:",self.doi)
        print(" Date of Return:",self.dor)
        if self.d4<=self.d2:
            print(" No Fine")
        else:
            print(" Fine: $",self.f)

l=library()
l.read()
l.calculate()


            
        
