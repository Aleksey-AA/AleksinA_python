print("1.Простая работа с print()")
print("Привет, мир!")
print(5,10,15,sep = " ")
print(f"10 + 25 = {10+25}")

print("2. Использование параметров sep и end в print()")
print(1,2,3,sep = " & ")
print("Python",end = " ")
print("лучший язык")

print("3. Форматированный ввод с F-строками")
x,y = 3.14,-8.14
print(f"Координаты точки: x = {x}; y = {y}")
name = input()
age = input()
print(f"Имя: {name}, Возраст: {age}")

print("4. Работа с input()")
name1 = input()
print(f"Привет, {name1}!")

print("5. Преобразование типов")
a = int(input())
b = int(input())
print(f"a + b = {a + b}")

print("6. Основы булевой логики")
print(5>3)
print(10<2)
print(7==7)
print(6!=8)
print(4>=4)
print(9<=3)
res = 8 > 12
print(res)
print(type(res))

print("7. Проверка четности и кратности числа")
x = 15
print(x % 2 == 0)
print(x % 5 == 0)
print(x % 3 == 0 and x % 5 == 0)

print("8. Работа с логическими операторами")
y = 4.5
print(y >= 1 and y <= 10)
print(0 <= y <= 5 or 10 <= y <= 15)
print(not(y < 5))

print("9. Приоритет логических операций")
print(True or False and False)
print(not False and True)
print(False or not True and True)
print(not(10 > 5 or 3 < 1))

print("10. Приведение типов к bool")
print(bool(0))
print(bool(-5))
print(bool(3.14))
print(bool(""))
print(bool("Python"))
print(bool(" "))

print("11. Дополнительное задание")
n = 6
print(n > 0)
print(n % 2 == 0)
print(n % 3 == 0)

print("12. Доступ к символам по индексу")
s = "Программирование"
print(s[0])
print(s[len(s)-1])
print(s[-1])
print(s[2], s[-2])

print("13. Обращение к символу с проверкой границ")
# print(s[100])
print("Ошибка: индекс выходит за границы ")
print(s[len(s)-1])

print("14. Создание срезов")
s2 = s[:6]
print(s2)
s3 = s[-5:]
print(s3)
s4 = s[2:7]
print(s4)
print(s[::2])
print(s[::-1])

print("15. Работа с шагом в срезах")
print(s[::3])
print(s[::-2])

print("16. Проверка неизменяемости строк")
# s[0] = "п"
print("Ошибка - строка это неизменяемый элемент, можно только пересоздать")
s5 = "P" + s[1:]
print(s5)

print("17. Дополнительное задание")
word = "abcdefgh"
w = word[2:5]
print(w)
print(word[::-1])
print(word[1:-1])