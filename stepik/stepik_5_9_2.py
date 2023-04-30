# Вводится список целых чисел в строку через пробел. С помощью list comprehension сформировать из них двумерный список
# lst размером N x N (квадратную таблицу чисел). Гарантируется, что из набора введенных чисел можно сформировать квадратную
# матрицу (таблицу). Результат отобразить в виде списка командой:  print(lst)
'''
Sample Input:
1 2 3 4 5 6 7 8 9
Sample Output:
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
'''
import math
lst_in = '1 2 3 4 5 6 7 8 9'
lst_in1 = lst_in.split()
N = int(math.sqrt(len(lst_in1)))
lst_out =[[int(x) for x in lst_in1[row*N:row*N+N:]] for row in range(N)]
print(lst_out)
