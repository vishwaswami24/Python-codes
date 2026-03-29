class custom:
    def __init__(self):
        print('constructor called')
    def __del__(self):
        print('destructor called')

c=custom()
print('HELLO')
