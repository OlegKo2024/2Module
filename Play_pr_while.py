# my_list = [0, 99, -5, 9]
# index = 0
# while index < len(my_list):
#     if my_list[index] >= 0:
#         print(my_list[index])
#         index += 1
#     else:
#         break
# 0
# 99
# Process finished with exit code 0
# попав на минус программа ушла на следующий пункт - break

# my_list = [0, 99, -5, 9]
# index = 0
# while index < len(my_list):
#     if my_list[index] >= 0:
#         print(my_list[index])
#         index += 1
#     else:
#         print('Я тут')
#         break
# 0
# 99
# Я тут
# Process finished with exit code 0
# Попав на минус программа ушла на следующий пункт условия print('Я тут') и далее на break

# my_list = [0, 99, 5, 9]
# index = 0
# while index < len(my_list):
#     if my_list[index] >= 0:
#         print(my_list[index], end='')
#         index += 1
#     else:
#         print('Я тут')
#         break
# 09959
# Process finished with exit code 0
# Здесь программа даже не дошла до следующего пункта условия, остановилась на конце значений

# my_list = [0, 99, 5, 9]
# index = 0
# while index < len(my_list):
#     if my_list[index] >= 0:
#         print(my_list[index], end=' ')
#         index += 1
#     else:
#         print('Я тут')
#         break
# 0 99 5 9
# Process finished with exit code 0

# my_list = [0, 99, -5, 9]
# index = 0
# while index < len(my_list):
#     if my_list[index] >= 0:
#         print(my_list[index], end=' ')
#         index += 1
#     else:
#         print('Я тут')
#         break
# 0 99 Я тут
# Process finished with exit code 0

# my_list = [0, 99, -5, 9]
# index = 0
# while index < len(my_list):
#     if my_list[index] >= 0:
#         print(my_list[index], end=' ')
#         index += 1
#         continue
#     elif my_list[index] < 0:
#         index += 1
#         continue
# print('Конец списка')
# 0 99 9 Конец списка
# Process finished with exit code 0

# my_list = [0, -99, 5, 9]
# index = 0
# while index < len(my_list):
#     if my_list[index] >= 0:
#         print(my_list[index], end=' ')
#         index += 1
#     else:
#         break
# 0, если my_list = [0, -99, 5, 9] - не выполнено условие, идет на else и на break
# Process finished with exit code 0

# my_list = [0, 99, 5, 9]
# index = 0
# while index < len(my_list):
#     if my_list[index] >= 0:
#         print(my_list[index], end=' ')
#         index += 1
#     else:
#         break
# print('Game is over')
# 0 99 5 9 Game is over, выполнено условие, но после +1, закончился список и программе перешла к строке 'Game is over'
# Process finished with exit code 0

my_list = [0, 99, 5, 9]
index = 0
while index < len(my_list):
    if my_list[index] >= 0:
        print(my_list[index], end=' ')
        index += 1
    else:
        break
print('Game is over')