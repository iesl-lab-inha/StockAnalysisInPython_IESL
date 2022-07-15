n, x = map(int, input('카드의 개수와 목표 값: ').split())
num = list(map(int, input('카드에 쓰여있는 수: ').split()))
sum_list = []
sum = 0

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            sum = num[i] + num[j] + num[k]
            if sum < x:
                sum_list.append(sum)
print(max(sum_list))
