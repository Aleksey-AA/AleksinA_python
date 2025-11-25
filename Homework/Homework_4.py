print('Методы строк')
print('1. Работа с регистром')
s = 'Python для автоматизации'
print('Строка s верхнем регистре: ',s.upper())
print('Строка s в нижнем регистре: ', s.lower())

print('2. Подсчет вхождений подстроки')
msg = 'абракадабра'
print(msg.count('ра'))
print(msg.count('а',3))

print('3. Поиск подстроки')
print(msg.find('ка'))
print(msg.rfind('а'))
print(msg.find('xyz'), ' -Подстрока не найдена, ошибки нет, вывод -1')

print('4. Замена подстроки')
text = 'Я изучаю Java'
print(text.replace('Java', 'Python'))
print(text.replace('Java', 'Python').replace(' ',''))

print('5. Проверка содержимого строки')
print('Python'.isalpha())
print('12345'.isdigit())
print('123abc'.isdigit())

print('6. Дополнение строк')
code = '42'
print(code.rjust(5,'0'))
print(code.ljust(10,'*'))

print('7. Разбиение строк')
s1, s2, s3 = 'яблоко, груша, банан'.split(', ')
print(s1)
print(s2)
print(s3)
print('яблоко, груша, банан'.split(', '))

print('8. Объединение списка в строку')
s4 = ['Привет', 'мир', '!']
print(' '.join(s4))
print(', '.join(['apple', 'banana', 'cherry']))
s5 = ', '.join(['apple', 'banana', 'cherry'])
print(s5)

print('9. Удаление пробелов')
print(" Python".lstrip())
print("Python ".rstrip())
print(" Python ".strip())

print('10. Дополнительное задание')
text1 = 'программирование'
print(text1.replace('п', 'П',1))
print(text1.count('р'))
print(text1.find('и'))
print(text1[::-1])

print('Спецсиволы')
print('1. Перевод строки')
s6 = 'Hellow\nPython'
print(s6)
print(r'\n в Python вляется спецсимволом переноса строки')

print('2. Горизонтальная табуляция')
t = 'Python\tAutomation'
print(t)
print(r'спецсимвол \r в Python обозначает табуляцию - горизонтальный отступ строки')

print('3. Экранирование символов')
path = 'C:\new\text.txt'
print(path)
print('Из-за присутствия в строке спецсиволов переноса строки и табуляции, строка выведена не так как была задумана')
path = 'C:\\new\\text.txt'
print(path)
print("Марка вина \"Ягодка\"")

print('4. Сырые (raw) строки')
path = r'C:\new\text.txt'
print(path)
print('В сырой строке, в отличие от обычной, Python не определяет спецсимволы')

print('5. Использование разных спецсимволов')
s = 'Hello\b World'
print(s)
print(r'Спецсимвол \b удалил символ перед ним')
s = 'Hello\fWorld'
print(s)

print('Форматирование строк')
print("Формирование строк через конкатенацию")
name = 'Aleksey'
age = '31'
nameage = 'Меня зовут ' + name + ', мне ' + age + ' год'
print(nameage)
# nameage = 'Меня зовут ' + name + ', мне ' + age + ' год' + 23
# print(nameage)
print('Появляется ошибка, т.к. при формировании строк через конкатенацию могут использоваться данные типа string')

print('Формирование строк с .format()')
d = 'Привет, меня зовут {0}, мне {1} год'.format(name, age)
print(d)
d = 'Привет, меня зовут {n}, мне {ag} год'.format(n = name, ag = age)
print(d)

d = 'Привет, меня зовут {0}, мне {1} год'.format(age, name)
print(d)

print('3. Использование F-строк')
city = 'Moscow'
year = "2025"
print(f'Сегодня {year} год, и я живу в {city}')
print(f'Через 5 лет будет {int(year) + 5} год')

print('4. Операции внутри F-строк')
print(f'Дважды мой возраст: {int(age)*2}')
print(f'Мое имя в верхнем регистре {name.upper()}')

print('5. Дополнительное задание')
currency = 'dollar'
rub = '92.5'
print('Курс валют: 1 {0} = {1} рубля'.format(currency, rub))
print(f'Квадрат числа 7 равен {7**2}')


