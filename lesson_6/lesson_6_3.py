# a = 18
# b = 15
#
# if a > b:
#     res = a
#     print(res)
# elif b > a:
#     res = b
#     print(res)
# else:
#     print('числа равны')

a = 14
b = 15

if a > b:
    res = a
else:
    res = b
print(res)

res = a + 10 if a > b else b
print(res)