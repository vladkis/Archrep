# Вводится список вещественных чисел. С помощью list comprehension сформировать список, состоящий из элементов введенного списка,
# имеющих четные индексы (то есть, выбрать все элементы с четными индексами). Результат вывести на экран в одну строку через пробел.
# data = input()
data = '8.5 11.3 1.0 -4.5 11.34 6.45'
ind = [float(x) for i,x in enumerate(data.split()) if i%2==0]
print(*ind)
