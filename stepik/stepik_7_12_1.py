'''
Подвиг 1. Вводится строка целых чисел через пробел. Напишите функцию, которая преобразовывает эту строку
в список чисел и возвращает их сумму.
Определите декоратор для этой функции, который имеет один параметр start - начальное значение суммы.
Примените декоратор со значением start=5 к функции и вызовите декорированную функцию для введенной строки s:
s = input()
Результат отобразите на экране.

Sample Input: 5 6 3 6 -4 6 -1
Sample Output: 26
'''
def start_sum(start):
    def s_decorator(fn):
        def wrapper(*args):
            result = fn(*args)+ start
            return result
        return wrapper
    return s_decorator



@start_sum(5)
def get_list(s):
    ls = list(map(int, s.split()))
    return sum(ls)


# s = input()
s = '5 6 3 6 -4 6 -1'
print(get_list(s))
