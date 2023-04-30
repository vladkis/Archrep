import sys

# считывание списка из входного потока
#lst_in = list(map(str.strip, sys.stdin.readlines()))
lst_in = ['5=отлично', '4=хорошо', '3=удовлетворительно']
# здесь продолжайте программу (используйте список lst_in)

lst1 = [lst_in[i].split('=') for i in range(len(lst_in))]
lst1.reverse()
dic = {(int(lst1[i][0]), lst1[i][1]) for i in range(len(lst1))}
print(*sorted(dic))

