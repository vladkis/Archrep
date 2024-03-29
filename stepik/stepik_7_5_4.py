'''


Большой подвиг 6. (Для закрепления предыдущего материала). Вводится таблица целых чисел (см. пример ниже) размером N x N элементов
(N определяется по входным данным). Эта таблица содержит нули, но кое-где - единицы. С помощью функции с именем verify, на вход
которой передается двумерный список чисел, необходимо проверить, являются ли единицы изолированными друг от друга, то есть, вокруг
каждой единицы должны быть нули.

Рекомендуется следующий алгоритм. В функции verify производить перебор двумерного списка. Для каждого элемента (списка)
со значением 1 вызывать еще одну вспомогательную функцию is_isolate для проверки изолированности единицы. То есть, функция
is_isolate должна возвращать True, если единица изолирована и False - в противном случае.

Как только встречается не изолированная единица, функция verify должна возвращать False. Если успешно доходим (по элементам списка)
до конца, то возвращается значение True.

Функцию выполнять не нужно, только определить.

P. S. При реализации функции is_isolate не следует прописывать восемь операторов if. Подумайте, как это можно сделать красивее
(с точки зрения реализации алгоритма).

Sample Input:

1 0 0 0 0
0 0 1 0 0
0 0 0 0 0
0 1 0 1 0
0 0 0 0 0

Sample Output:   True

'''
# import sys

# считывание списка из входного потока
# s = sys.stdin.readlines()
# lst_in = [list(map(int, x.strip().split())) for x in s]
lst_in = [[1, 0, 0, 0, 0], [0, 0, 1, 0, 0], [
    0, 0, 0, 0, 0], [0, 1, 0, 1, 0], [0, 0, 0, 0, 0]]


def is_isolate(lst_in, i, j):
    sm1 = lst_in[i-1][j-1] + lst_in[i-1][j] + lst_in[i-1][j+1]
    sm2 = lst_in[i+1][j-1] + lst_in[i+1][j] + lst_in[i+1][j+1]
    sm3 = sm1 + sm2 + lst_in[i][j-1] + lst_in[i][j+1]
    if sm3 == 0:
        return True
    else:
        return False


def verify(lst_in):
    for i in range(len(lst_in)):
        for j in range(len(lst_in)):
            if not is_isolate(lst_in, i, j):
                return False
            else:
                return True


print(verify(lst_in))


# здесь продолжайте программу (используйте список lst_in)
# suma = []
# flag1 = True
# for i in range(4):
#     suma = []
#     for j in range(5):
#         suma.append(lst_in[i][j] + lst_in[i + 1][j])
#     if (('1, 1' in str(suma)) or ('2' in str(suma))) and flag1:
#         flag1 = False
#         print('НЕТ')
#         break
# if flag1:
#     print('ДА')
