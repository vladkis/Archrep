
# def sieve(n):
#     primes = []
#     temp_list = [0 for x in range(0, n)]
#     i, j = 2, 2
#     while (i*j < n):
#         temp_list[i*j] = 1
#         j = j+1
#         if i*j >= n:
#             i, j = i+1, 2
#     for i in range(3, n):
#         if temp_list[i] == 0:
#             primes.append(i)
#     return primes

# if __name__ == '__main__':
#     n = int(input('Введите число '))
#     print(*sieve(n))


# def prime_num():
#     nm = 9
#     while True:
#      #   sq = int(nm**0.5)
#         for i in range(2, nm):
#             if nm % i == 0:
#                 break
#             else:
#                 yield nm
#         nm += 1

# b = prime_num()
# for i in range(2,20):
#     print(next(b), end='')


# Подвиг 5. Определите функцию-генератор, которая бы возвращала простые числа.
# (Простое число - это натуральное число, которое делится только на себя и на 1).
# Выведите с помощью этой функции первые 20 простых чисел (начиная с 2) в одну строчку через пробел.

from math import sqrt


def is_prime(n):
    if (n <= 1):
        return False
    if (n == 2):
        return True
    if (n % 2 == 0):
        return False

    i = 3
    while i <= sqrt(n):
        if n % i == 0:
            return False
        i = i + 2
    return True

def prime_generator():
    n = 1
    while True:
        n += 1
        if is_prime(n):
            yield n

generator = prime_generator()
for i in range(20):
    print(next(generator), end=' ')
