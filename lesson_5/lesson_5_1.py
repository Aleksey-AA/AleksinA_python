# streets = ['Ломоносова','Ленина','Артихиной']
# ages = [23, 54, 26]
#
# """
#        0          1          2
# ['Ломоносова','Ленина','Артихиной']
#        -3         -2         -1
# """

# print(streets[-2])
# print(streets[2])
# print(streets[-1])

# avg_ages = int(sum(ages)/len(ages))
# print(avg_ages)

# ages[1] = 31
# print(ages)
# lst = ['Волгоград', 332, 21.343, True, False, [2, 3, 4, 'wrgerg']]

lst = []
lst2 = list()
lst3 = list('Волгоград')
# print(len(lst3))
# print(max(ages))
# print(min(ages))
# print(sum(ages))
# print(sorted(lst3))
# print(sorted(ages))
# # print(lst3)
# print(sorted(ages, reverse = True))

# print(sum(lst3))

streets = ['Ломоносова','Ленина','Артихиной']
ages = [23, 54, 26]
# print(streets + ages)
result = streets + ages
# print(result)
# print(result + ["А"])
# print(result * 2)
# print('Ломоносова' in result)
# print('Ломо' in result)
# print(54 in result)

result.append('1234')
# print(result)
result.append([1,2])
print(result)
# print([1, 2] in result)

del result[-1]
del result[1]
del result[1]
print(result)

