'''
Великий подвиг 8. Вводится список из целых чисел в одну строчку через пробел. Необходимо выполнить его сортировку по возрастанию
с помощью алгоритма сортировки слиянием. Функция должна возвращать новый отсортированный список.
Вызовите результирующую функцию сортировки для введенного списка и отобразите результат на экран в виде последовательности чисел,
записанных через пробел.

Подсказка. Для разбиения списка и его последующей сборки используйте рекурсивные функции.
P. S. Теория сортировки в видео предыдущего шага.


Sample Input:  8 11 -6 3 0 1 1

Sample Output:  -6 0 1 1 3 8 11

'''


def sort_merg(lst):
    if len(lst) == 1:                                # условие выхода из рекурсии
        return lst                                   # выход из рекурсии
    cent = len(lst)//2                               # поиск середины списка
    left_lst = sort_merg(lst[:cent])                 # рекурсивный запуск на деление первой части
    right_lst = sort_merg(lst[cent:])                # рекурсивный запуск на деление второй части
    return combine_lst(left_lst, right_lst, [])      # запуск функции слияния списков


def combine_lst(lst_a, lst_b, comb):
    if len(lst_a+lst_b) > 0:                        # пока в списках что то есть
        a, b = lst_a[:1], lst_b[:1]                 # присвоим значения срезами, на случай пустого
        if a and a >= b:
            comb.append(lst_a.pop(0))               # добавляем в список слияния большее
        if b and b >= a:
            comb.append(lst_b.pop(0))               # добавляем в список слияния большее
        return combine_lst(lst_a, lst_b, comb)      # рекурсивно запускаем повтор
    else:
        return comb                                 # возвращаем комбинированый список


lst = [int(i) for i in input().split()]             # ввод с клавиатуры
print(*sort_merg(lst)[::-1])                        # вывод результата функции
