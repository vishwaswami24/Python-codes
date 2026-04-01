
f=open('filedemo')
'''
#read mode

f=open('filedemo','r')

#print('whole data:',f.read())
#print('first 20 characters:',f.read(20))
#print('first line of data:',f.readline())
#print('content in list format:',f.readlines())
#print('specific content in list format:',f.readlines(15))
d=f.readlines()
print('show as list content:',d)
#print('show specific line as list content:',d[0])

#write mode

f=open('filedemo','w')

f.write('Monty Python Flying Circus')
f.close()                 #important to close file to update its contents

#append mode
f=open('filedemo','a')

f.write('\nGuido Van Rossum')
f.close()

#store data permenant

number=input('Mobile Number:')
f=open('Mobile number','a')
data=number+'\n'
f.write(data)
f.close()
'''
#exclusive create mode
f=open('exclusive file','x')
f.close()



