'''
class stud:
    
    def greet(self):     #class method
        print('Hello')


s=stud()          #object creation
s.greet()         #using class method

print(type(s))    #user defined data type
'''
class student: 

    institute='Government Polytechnic'     #static data member
    city='Latur'
    def get(self):
        self.name=input('Enter name:')           #dynamic data member
        self.roll=input('Enter roll number:')
     
    def display(self):
        print('Institute name:',self.institute)
        print('Institute city:',self.city)
        print('Student name:',self.name)
        print('Student roll number:',self.roll)
      
s=student()
s.get()
s.display()
student.city='Pune'
s.display()

