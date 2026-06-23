s={2,'pune',4.5,-2,2}

print(s)
print(type(s))
print(len(s))

for i in s:
    print(i)

s.add(9)
print(s)

s.remove(2)
print(s)

l=[9,8,4,3]
s.update(l)
print(s)

s1={10,20,60}
s.update(s1)
print(s)

s.remove(20)
print(s)

s.discard(-2)
print(s)


