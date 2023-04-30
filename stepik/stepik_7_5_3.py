"""
Подвиг 5. Объявите функцию с именем get_data_fig для вычисления периметра произвольного N-угольника.
На вход этой функции передаются N длин сторон через аргументы. Дополнительно могут быть указаны именованные аргументы:

type - булево значение True/False
color - целое числовое значение
closed - булево значение True/False
width - целое значение

Функция должна возвращать в виде кортежа периметр многоугольника и указанные значения именованных параметров
в порядке их перечисления в тексте задания (если они были переданы). Если какой-либо параметр отсутствует,
его возвращать не нужно (пропустить).

Функцию выполнять не нужно, только определить.

"""
def get_data_fig(*N, **kwargs):
    perimetr = sum(N)
    t = (perimetr,)
    if "type" in kwargs:
        typ_e = kwargs["type"]
        t += (typ_e,)
    if "color" in kwargs:
        color = kwargs["color"]
        t += (color,)
    if "closed" in kwargs:
        closet = kwargs["closed"]
        t += (closet,)
    if "width" in kwargs:
        width = kwargs["width"]
        t += (width,)
    return t

# Еще одно решение
# def get_data_fig(*args, **kwargs):
#     return (sum(args),) + tuple(kwargs[i] for i in ['type', 'color', 'closed', 'width'] if i in kwargs)
