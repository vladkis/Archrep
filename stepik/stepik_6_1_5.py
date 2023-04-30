# put your python code here
#lst =input().split()
lst = ['вологда=город', 'house=дом', 'True=1', '5=отлично', '9=божественно']
lst1 = [lst[i].split('=') for i in range(len(lst))]
d=dict(lst1)
key_control = ['house', 'True', '5']
#for i in range(len(key_control)):
 #   d[key]==key_control[i]

print(d.keys())
