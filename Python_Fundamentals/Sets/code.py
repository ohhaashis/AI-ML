s = {1,2,3,4,5}

print(type(s))
print(s)
print(len(s))
s.add(6)
print(s)

empty_set = set()
print(type(empty_set))

print(s.remove(6))
print(s)

# s.clear()
# print(s)

t = {1,3,6,8,9}

print(s.union(t))
print(s.intersection(t))