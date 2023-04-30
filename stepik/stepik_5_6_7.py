# lst = list(map(int, input().split()))
lst = [4, 5, 2, 0, 6, 3, -56, 3, -1]
i = 1
N = len(lst)
for i in range(N - 1):
    for j in range(len(lst)-i-1):
        if lst[j]>lst[j+1]:
            lst[j],lst[j+1] =  lst[j+1],lst[j]
print(*lst)
