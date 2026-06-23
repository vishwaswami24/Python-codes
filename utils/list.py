
l1=[10,20,20,'abd',12.4,-30]

r=l1[1:5:1]
print(r)

r1=l1[::]
print(r1)

l1.append(True)
print(l1)

l1.insert(2,30)
print(l1)

l1.pop()
print(l1)

l1.pop(2)
print(l1)

l1.remove(20)
print(l1)

    

l2=l1*2
print(l2)
