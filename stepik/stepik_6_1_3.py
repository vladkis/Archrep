# lst =input().split()
lst = 'one=1', 'two=2', 'three=3'
lst1 = [lst[i].split('=') for i in range(len(lst))]
#d = dict(lst1)
#for key in d:
#    d[key] = int(d[key])
#print(*sorted(d.items()))
print(lst)
print(lst1)
