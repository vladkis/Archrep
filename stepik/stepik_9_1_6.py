# Подвиг 8. Имеется список из названий городов:
# cities = ["Москва", "Ульяновск", "Самара", "Уфа", "Омск", "Тула"]
# Необходимо записать генератор, который бы используя этот список, выдавал 1 000 000
# наименований городов по циклу. То есть, дойдя до конца списка, возвращался в начало
# и повторял перебор. И так, для выдачи миллиона названий.
# Вывести на экран первые 20 наименований городов с помощью генератора в одну строчку через пробел.


cities = ["Москва", "Ульяновск", "Самара", "Уфа", "Омск", "Тула"]

gen = (citi for citi in cities*(100000//len(cities)))
i = 0
for x in gen:
    if i < 20:
        print(x, end=' ')
        i += 1
