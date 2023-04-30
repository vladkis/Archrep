lst =input().split()
lst1 = [lst[i].split('=') for i in range(len(lst))]
d = dict(lst1)
if 'False' in d:
    del d['False']
if '3' in d:
    del d['3']
print(*sorted(d.items()))
