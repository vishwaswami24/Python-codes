c = 0
d = {'a': 'ant', 'b': 'ball', 'c': 'cat', 0: 'rest'}
print(d)
print(type(d))
print(len(d))
print(d.keys())
print(list(d.__iter__()))  # ['a', 'b', 'c', 0]
print(d.values())
print(d.setdefault(0))
for i in d:
    print(i, ':', d[i])

d[1] = 'active'

d1 = {2: 2, 'b': 'bat'}
d.update(d1)
print(d)
d.pop(2)
d.popitem()
print(d)
x = (1, 2)
d = d.fromkeys(x)
print(d)
print(list(iter(reversed(d.items()))))

for i, j in d.items():
    print(list((i, j)))

d.clear()