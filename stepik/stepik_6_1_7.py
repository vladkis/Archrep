lst=['+71234567890', '+71234567854', '+61234576890', '+52134567890', '+21235777890', '+21234567110', '+71232267890']
#lst =input().split()
lst1=[[lst[i][:2],[lst[i][2:len(lst[i])]]] for i in range(len(lst))]
d=dict(lst1)
#lst2=[[lst1[i][:2]]for i in range(len(lst1))]

key=lst1[0][0]
tel=lst[0][1]
i=1
for i in range(len(lst1)-1):
    if lst1[i][0]==key:
        lst1[0][1].append(lst1[i][1])
 #       del lst1[i]

# k=[]
# lst2=[[]]
# [k.append(x[0]) for x in lst1 if x[0] not in k]
# for x in k:
#     lst2.append(x)
#     for y in lst1:
#         if y[0]==x and y[1] not in lst2[[1]]:
#             lst2.append(y[1])

# k=k.append([1,2,3])
print(lst1)
#print(k)
#print(lst2)
