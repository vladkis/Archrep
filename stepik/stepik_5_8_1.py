# Вводятся вещественные числа в строку через пробел. Необходимо на их основе сформировать список lst с помощью list comprehension
# (генератора списков) из модулей введенных чисел (в списке должны храниться именно числа, а не строки). Результат вывести на экран
# в виде списка командой: print(lst)

st = '5.56 -8.7 1.0 3.14 77.845'
lst = [abs(float(x)) for x in st.split()]
print (*lst)