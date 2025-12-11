print('УСЛОВНЫЙ ОПЕРАТОР')
print('1. Проверка знака числа')
x = int(input('Введите число x: '))

if x > 0:
    print('Число положительное')
else:
    if x < 0:
        print('Число отрицательное')
    else:
        print('Число равно нулю')

print('2. Проверка на четность')
x = int(input('Введите число x: '))

if x % 2 == 0:
    print('Число четное')
else:
    print('Число нечетное')

print('3. Определение диапазона')
x = int(input('Введите число x: '))

if 1 <= x <= 10:
    print('Число находится в диапазоне')
else:
    print('Число вне диапазона')

print('4. Перестановка двух чисел')
a = int(input('Введите число a: '))
b = int(input('Введите число b: '))

if a < b:
    a, b = b, a
print(a, b)

print('5. Поиск минимума из двух чисел')
a = int(input('Введите число a: '))
b = int(input('Введите число b: '))

if a < b:
    print(a)
else:
    if b < a:
        print(b)
    else:
        print('Числа равны')

print('6. Проверка наличия элемента в списке')
marks = [3, 4, 5, 2, 5, 4]

if 2 in marks:
    print('Есть неудовлетворительная оценка')
else:
    print('Все оценки положительные')

print('7. Проверка делимости')
x = int(input('Введите число x: '))

if x % 3 == 0 and x % 5 == 0:
    print('Число делится на 3 и 5')
else:
    if x % 3 == 0:
        print('Число делится только на 3')
    else:
        if x % 5 == 0:
            print('Число делится только на 5')
        else:
            print('Число не делится на 3 и 5')

print('8. Оператор in для проверки пароля')
password = input('Введите пароль: ')

if password == 'admin123':
    print('Доступ разрешен')
else:
    print('Доступ запрещен')

print('9. Калькулятор скидки')
amount = float(input('Введите сумму покупки: '))
if amount >= 5000:
    amount = amount - (amount * 0.1)
    print(amount)
else:
    if 5000 > amount >= 1000:
        amount = amount - (amount * 0.05)
        print(amount)
    else:
        print(amount)

print('10. Определение високосного года')
year = int(input('Введите год: '))

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print('Год високосный')
else:
    print('Год не високосный')

print('ВЛОЖЕННЫЕ УСЛОВИЯ И elif')
print('1. Проверка оценки')
est = int(input('Введите оценку: '))
if est == 5:
    print('Отлично!')
elif est == 4:
    print('Хорошо')
elif est == 3:
    print('Удовлетворительно')
elif est == 2 or est == 1:
    print('Неудовлетворительно')
else:
    print('Некорректная ошибка')

print('2. Определение времени суток')
hour = int(input('Введите час времени суток от 0 до 23: '))

if 6 <= hour <= 12:
    print('Утро')
elif 12 <= hour <= 17:
    print('День')
elif 18 <= hour <= 21:
    print('Вечер')
elif 22 <= hour <=23 or 0 <= hour <=5:
    print('Ночь')
else:
    print('Некорректное время')

print('3. Классификация температуры')
temp = int(input('Введите значение температуры: '))

if temp < -10:
    print('Очень холодно')
elif -10 <= temp <= 0:
    print('Холодно')
elif 1 <= temp <= 10:
    print('Прохладно')
elif 11 <= temp <= 25:
    print('Тепло')
elif temp > 25:
    print('Жарко')

print('4. Проверка года на високосность')
year = int(input('Введите год: '))

if year % 4 == 0 and year % 100 != 0:
    print('Год високосный')
elif year % 400 == 0:
    print('Год високосный')
else:
    print('Год не високосный')

print('5. Калькулятор двух чисел')
num1 = float(input('Введите первое число: '))
num2 = float(input('Введите второе число: '))
symbol = input('Введите знак операции (+,-,*,/): ')

if symbol == '+':
    print(num1 + num2)
elif symbol == '-':
    print(num1 - num2)
elif symbol == '*':
    print(num1 * num2)
elif symbol == '/':
    if num2 != 0:
        print(num1 / num2)
    else:
        print('Ошибка: деление на ноль!')
else:
    print('Неизвестная операция')

print('ТЕРНАРНЫЙ ОПЕРАТОР')
print("1. Проверка четности числа")
x = int(input('Введите число x: '))
print('Число х четное') if x % 2 == 0 else print('Число х нечетное')

print('2. Определение наибольшего числа')
a = int(input('Введите число a: '))
b = int(input('Введите число b: '))

print('Наибольшее число а: ', a) if a > b else print('Наибольшее число b: ', b)

print('3. Проверка положительного или отрицательного числа')
x = int(input('Введите число x: '))

print("х положительное число") if x > 0 else (print('х отрицательное число') if x < 0 else print('x = 0'))

print('4. Определение возраста для входа в клуб')
age = int(input('Введите свой возраст: '))

print('Вход разрешен') if age >= 18 else print('Вход запрещен')

print('5. Определение скидки в магазине')
s = float(input('Введите сумму покупки: '))

s = s - (s * 0.1) if s > 5000 else s
print(s)
