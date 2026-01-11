# sum_1 = 1 + 2 + 3 + 4 + 5
# print(sum_1)

# num = 1000
# sum_2 = 0
# i = 1
#
# while i <= 1000:
#     sum_2 += i
#     i += 1
#
# print(sum_2)

# correct_password = 'Пароль123'
# input_password = input('Введите пароль: ')
#
# while input_password != correct_password:
#     print('Пароль не верный, введите еще раз')
#     input_password = input('Введите пароль: ')
#
# print('Пароль верный')

correct_password = 'Пароль123'
input_password = input('Введите пароль: ')
counter = 1

while input_password != correct_password:
    print('Пароль не верный, введите еще раз')
    input_password = input('Введите пароль: ')
    counter += 1
    if counter == 3:
        print('Пароль введен неправильно 3 раза, программа завершена')
        break

print('Пароль верный')
