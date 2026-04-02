str = input('Enter string:')
rstr = str[-1::-1]
print(str)
print(rstr)

if str==rstr:
    print('palindrome')
else:
    print('not palindrome')
