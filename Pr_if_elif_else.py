# На вход программе подаются 3 целых числа и записываются в переменные first, second и third соответственно.
# Ваша задача написать условную конструкцию (из if, elif, else), которая выводит кол-во одинаковых чисел среди 3-х введённых.
#
# Пункты задачи:
# Если все числа равны между собой, то вывести 3
# Если хотя бы 2 из 3 введённых чисел равны между собой, то вывести 2
# Если равных чисел среди 3-х вообще нет, то вывести 0

number_1=int(input('Введите первое число: '))
number_2=int(input('Введите второе число: '))
number_3=int(input('Введите третье число: '))

if number_1 == number_2 == number_3:
    print(3)
elif number_1 == number_2 or number_1 == number_3 or number_2 == number_3:
    print(2)
else:
    print(0)