'''
Подвиг 3. На вход программы поступает строка из целых чисел, записанных через пробел.
Напишите функцию get_list, которая преобразовывает эту строку в список из целых чисел
и возвращает его. Определите декоратор для этой функции, который сортирует список чисел
по возрастанию. Результат сортировки должен возвращаться при вызове декоратора.

Вызовите декорированную функцию get_list и отобразите полученный отсортированный список lst командой:
print(*lst)

Sample Input:  8 11 -5 4 3 10

Sample Output:  -5 3 4 8 10 11
'''


def sort_decorator(fn):
    def wrapper(*args):
        sl = fn(*args)
        return sorted(sl)
    return wrapper

@sort_decorator
def get_list(s):
    return list(map(int, s.split()))

s = '8 11 -5 4 3 10'
lst = get_list(s)
print(*lst)

'''
# определяем декоратор sort_decorator, который принимает на вход функцию func
def sort_decorator(func):
    # Определяем внутреннюю функцию-обертку wrapper, которая принимает на вход произвольное число позиционных и именованных аргументов.
    def wrapper(*args, **kwargs):
         # Выполняем функцию func с переданными аргументами и сохраняем результат в переменную result.
        result = func(*args, **kwargs)
        # Возвращаем отсортированный результат.
        return sorted(result)
    # Возвращаем функцию-обертку.
    return wrapper
# Декорируем функцию get_list декоратором sort_decorator, чтобы отсортировать список чисел по возрастанию.
@sort_decorator
# Определяем функцию get_list, которая принимает на вход строку s.
def get_list(s):
    # Преобразуем строку в список целых чисел и возвращаем его.
    return list(map(int, s.split()))
s = input()
# Вызываем функцию get_list, чтобы преобразовать строку в список целых чисел.
lst = get_list(s)
# Выводим отсортированный список на экран с помощью команды print(*lst), которая распаковывает список в отдельные аргументы для функции print.
print(*lst)
'''