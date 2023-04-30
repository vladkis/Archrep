"""

Подвиг 4. Объявите функцию, которая принимает строку на кириллице и преобразовывает ее в латиницу,
используя следующий словарь для замены русских букв на соответствующее латинское написание:

t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
     'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
     'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh',
     'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}

Функция должна возвращать преобразованную строку. Замены делать без учета регистра (исходную строку
перевести в нижний регистр - малые буквы). У функции также определить формальный параметр sep
с начальным значением в виде строки "-". Он будет определять символ для замены пробелов в строке.

После объявления функции прочитайте (с помощью функции input) строку и дважды вызовите функцию
(с выводом результата ее работы на экран):

- первый раз только со строкой
- второй раз со строкой и именованным аргументом sep со значением '+'.

Sample Input:  Лучший курс по Python!

Sample Output:  luchshiy-kurs-po-python!
                luchshiy+kurs+po+python!

"""

t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
     'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
    'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh',
    'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}


h = "лучший курс по Python!"     #input().lower()

def get_str(str, sep = '-'):
    for i, j in enumerate(str):  # Перебираем индекс, значение в str
        if j in t:
            str[i] = t[j]
        if j == ' ':
            str[i] = sep
    return ''.join(str)


g = list(map(str,h))
print(get_str(g, '-'))

g = list(map(str,h))
print(get_str(g, '+'))

# print(h)
# print(g)
