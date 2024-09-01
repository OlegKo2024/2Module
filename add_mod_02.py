print('Генератор пароля')
def random_number(s, f):
    import random
    n = random.randrange(s, f)
    return n
def pair_number():
    for i in range(1, n):
        for j in range(i, n):
            if n % (i + j) == 0 and i != j:
                print(i, j, end=' ')



n = random_number(3, 20)
print(n)
pair_number()

print('Генератор паролей для всех чисел')
n = 3
while n <= 20:
    for i in range(1, n):
        for j in range(i, n):
            if n % (i + j) == 0 and i != j:
                print(f'{n} - {i}{j}')
    n += 1
