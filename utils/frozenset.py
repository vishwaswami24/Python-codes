s={'python',12,50,-50}
t=(1,'abc',-8)
l=[12,'java',True]

s1=frozenset(s)
print(s)

s2=frozenset(t)
print(t)

s3=frozenset(l)
print(l)

f=s1.union(s2)
print(f)

f1=f.union(s3)
print(f1)
