arr = ['0']
i = input()
arr.append(i[0])
arr.append(i[1])
cnt = 0
while(True):
    cnt += 1
    temp = arr[-1] + arr[-2]
    temp.zfill(2)
    arr.append(temp[1])
    if arr[0]==arr[-2] and arr[1]==arr[-1]:
        break
print(cnt)