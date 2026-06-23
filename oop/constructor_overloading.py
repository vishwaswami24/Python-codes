class A:
    def __init__(self):
        print('Inside constructor A')
class B(A):
    def __init__(self):
        super().__init__()
        print('Inside constructor B')
        
b=B()        
