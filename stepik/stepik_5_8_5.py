# Вводится натуральное число n. Необходимо сформировать список с помощью list comprehension, состоящий из делителей числа n
# (включая и само число n). Результат вывести на экран в одну строку через пробел.
# N =int(input())
N = 10
divider = [x for x in range(1,N+1) if N % x == 0]
print(*divider)
