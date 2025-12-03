a = [21, 54, 6.44, 6, 3, 2, 7675, 35003509, 3424]
print(a)
a.append(678)
a.append('ere')
a.append(True)
a.append([True, False])
a.append(True)
a.insert(1, 66)
# print(a)

# a.remove(True)
# a.remove(True)

# last_el = a.pop()
# print(a)
# print(last_el)

# index_el = a.pop(3)
# print(a)
# print(index_el)

# a.clear()
# print(a)
# b = [:]
# b = list(a)
b = a.copy()
# print(id(a))
# print(id(b))
# print(a)
# # print(a.count(True))
# # print(a.index(True, 13))
# a.reverse()
# print(a)

c = [21, 54, 6.44, 6, 3, 2, 7675, 35003509, 3424]
c.sort(reverse=True)
print(c)

d = sorted(c)
print(d)