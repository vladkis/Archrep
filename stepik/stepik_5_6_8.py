# n=int(input())
n = 221
lst = [1, 2, 4, 8, 16, 32, 64]
lst1 = lst[::-1]
lst2 = []
j = 1
for i in range(len(lst1)):
    for j in range(n//lst1[i]):
        lst2.append(lst1[i])
    n = n%lst1[i]
print(lst2)
