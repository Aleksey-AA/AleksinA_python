print("Работа с целыми и вещественными числами")
a = 8
b = 3
x = 2.5
y = -1.7
print(a,type(a))
print(b,type(b))
print(x,type(x))
print(y,type(y))

print("Основные арифметические операции")
num1 = 12
num2 = 5
print("num1 + num2 =", num1 + num2)
print("num1 - num2 =", num1 - num2)
print("num1 * num2 =",num1 * num2)
print("num1 / num2 =",num1 / num2)
print("num1 // num2 =",num1 // num2)
print("num1 % num2 =",num1 % num2)
print("num1 / num2 =",num1 ** num2)

print("Особенности работы с делением")
a = 10
b = 3
c = a / b
d = a//b
e = a%b
print("c =", c)
print("d =", d)
print("e =", e)

print("Работа с приоритетом операторов")
print("5 + 3 * 2 =", 5 + 3 * 2)
print("(5 - 3) * 2 =", (5 - 3) * 2)
print("10 / 2 ** 2 =", 10 / 2 ** 2)

print("Использование сокращенных операторов")
count = 10
count += 5
count -= 3
count *= 2
count /= 4
print("count =", count)

print("СТРОКИ PYTHON")
print("Создание строк")
s1 = "Python"
s2 = "Программирование"
print(s1)
print(s2)
s3 = """
Алексин
Алексей
Андреевич
"""
print(s3)
empty = ""
print("Длина строки empty",len(empty))

print("Конкатенация строк")
first_name = "Иван"
last_name = "Петров"
full_name = first_name + " " + last_name
print(full_name)

print("Преобразование типов")
s = "Возраст: "
age = 25
t = s + str(age)
print(t)

print("Дублирование строк")
print("xa " * 5)
# print("xa " * 2.5)

print("Длина строки")
text = "Привет, мир!"
print("количество символов ", len(text))
q = ""
print("количество символов q ", len(q))

print("Проверка вхождения подстроки")
sentence = "Я изучаю Python"
w = "Python"
print("Python" in sentence)
print("Java" in sentence)
print(w in sentence)

print("Сравнение строк")
a = "apple"
b = "banana"
print(a == b)
print(a != b)
print(a < b)
print(a > b)
print(a <= b)
print(a >= b)

print("Код символов")
print("код символа А ",ord("А"))
print("код символа а ",ord("а"))
print("код символа Я ",ord("Я"))







