# name=input('Введите ваше имя:')
# if name=='Dave':
#     print('Hi, ',name,sep='')
# print('Привет, ',name,sep='') # если Dave, вывод обоих принт, если иное, то первый принт в условии:
#
# # name=input('Введите ваше имя:')
# if name=='Dave':
#     print('Hi, ',name,sep='')
# else:
#     print('Привет, ',name,sep='') # сейчас ИЛИ
#
# # name = input('Введите ваше имя:')
# if name=='Dave':
#     print('Hi, ', name,sep='')
# if name==('Dan'):
#     print('Hello, Mr. ',name,sep='')
# else:
#     print('Привет, ', name,sep='')  # сейчас ИЛИ, но это не очень верно в ситуации множественного перебора и одинакового ответа

number=int(input('Введите число: '))
if number % 3 == 0 and number % 5 == 0:
    print('FizzBuss')
elif number % 3 == 0:
    print(Fizz)
elif number % 5 == 0:
    print(Buzz)
else:
    print('Не делится')

number=int(input('Введите число: '))
if number % 3 == 0 or number % 5 == 0:
    print('Делится')
else:
    print('Не делится')

# https://peps.python.org/pep-0008/ - PEP 8 - руководство по стилю кода в Python