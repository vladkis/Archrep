# Вводятся два списка целых чисел одинаковой длины каждый с новой строки. С помощью list comprehension сформировать третий список,
# состоящий из суммы соответствующих пар чисел введенных списков. Результат вывести на экран в одну строку через пробел.
l1 = [1, 2, 3, 4, 5]
l2 = [6, 7, 8, 9, 10]

#l1 = list(map(int, input().split()))
#l2 = list(map(int, input().split()))
l3 = [(v1 + l2[i1]) for i1, v1 in enumerate(l1)]

print(*l3)
