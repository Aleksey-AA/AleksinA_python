from lesson_5.lesson_5_1 import result

print('Списки')

print('1. Создание списков')
cities = ['Москва', 'Тверь', 'Вологда']
numbers = [1, 2, 3, 4, 5]
mixed = [34, 'st', False, 62.543]

print('2. Доступ к элементам списка')
print(cities[0])
print(numbers[-1])
# print(cities[10])
print('Ошибка индекс эдемента вышел за границы списка')

print('3. Изменение элементов списка')
numbers[1] = 10
print(numbers)
mixed[-1] = 'Python'
print(mixed)

print('4. Функции для работы со списками')
print(len(numbers))
print(max(numbers))
print(sum(numbers))
print(sorted(numbers))
print(sorted(numbers, reverse=True))

print('5. Операции со списками')
print([1, 2, 3] + [4, 5])
print(['Python', 'is', 'awesome'] * 3)

print('6. Проверка вхождения')
print(3 in numbers)
print('Москва' in cities)
print([1, 2] in mixed)

print('7. Удаление элеменетов')
del numbers[2]
print(numbers)
del cities[-1]
print(cities)

print('8. Дополнительное задание')
p = list('Python')
print(p)
print(max(p))
print(min(p))
# print(sum(p))
print('Ошибка - нельзя складывать элементы списка типа string')

print('Срезы списков')
print('1. Создание и копирование списков')
gor = ['Уфа', 'Омск', 'Елец', 'Анапа', 'Тюмень']
g = gor[:]
print(id(gor))
print(id(g))
print('ID списков разные - объекты являются разными копиями')

print('Извлечение элементов с помощью срезов')
print(gor[1:3])
print(gor[3:])
print(gor[:3])
print(gor[:])
print(gor[-2:])

print('3. Использование шагов в срезах')
print(gor[1::2])
print(gor[::-1])
print(gor[-2::-2])

print('4. Изменение элементов списка через срезы')
gor[1:3] = 'Сочи', 'Нижний Новгород'
print(gor)
gor[1::2] = ['Город']*len(gor[1::2])
print(gor)
gor[1:3] = 'Волгоград', 'Омск'
print(gor)

print('5. Операции с объединением списков')
result = [1, 2, 3] + [4, 5, 6]
print(result)
print(['Python', 'rocks'] * 2)

print('6. Сравнение списков')
print([1, 2, 3] == [1, 2, 3])
print([10, 5, 3] > [5, 10, 3])
# print([1, 2, 3] < [1, 2, 'abc'])
print('Нельзя использовать сравнение < и > в списках с разными типами int и str - ошибка')

print('7. Дополнительное задание')
chars = list('Python')
print(max(chars))
print(min(chars))
# print(sum(chars))
print('Элементы списка типа str нельзя суммировать - ошибка')

print('Методы списков')
print('1. Добавление элементов')
numbers = [5, 10, 15]
numbers.append(20)
numbers.insert(1,7)
numbers.append('Python')
print(numbers)

print('2. Удаление элементов')
numbers.remove(10)
last = numbers.pop()
print(last)
in1 = numbers.pop(1)
print(in1)
numbers.clear()
print(numbers)

print('3. Копирование списков')
letters = ['a', 'b', 'c']
l = letters.copy()
lt = list(letters)
print(id(letters))
print(id(l))
print(id(lt))
print('Оригинальный список и копии разные объекты - id разный')

print('4. Поиск элементов')
marks = [2, 3, 5, 3, 4, 5, 2, 3]
print(marks.count(3))
print(marks.index(5))
print(6 in marks)

print('5. Изменение порядка элементов')
nums = [8, 2, 5, 1, 7]
nums.sort()
print(nums)
nums.sort(reverse=True)
print(nums)
nums.reverse()
print(nums)

print('6. Сортировка строк')
cities = ['Уфа', 'Омск', 'Елец', 'Анапа', 'Тюмень']
cities.sort()
print(cities)
ci = sorted(cities)
print(ci)

print('7. Дополнительное задание')
chars = list('programming')
print(chars.count('g'))
chars.reverse()
print(chars)
chars.sort()
print(chars)
print('Порядок букв отсортирован по алфавиту')

print('Вложенные списки (массивы)')
print('1. Создание вложенного списка')
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]
print(matrix)
print(matrix[1])
print(matrix[2][0])

print('2. Изменение элементов вложенного списка')
matrix[0] = [0, 0, 0, 0]
matrix[1][-1] = 'Python'
print(matrix)
