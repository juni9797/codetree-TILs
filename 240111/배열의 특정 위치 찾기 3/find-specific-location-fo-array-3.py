num = list(map(int, input().split()))

new_list = []
for i in range(0, len(num)+1):
    if num[i] != 0:
        new_list.append(num[i])
    else:
        break

print(new_list[-1]+new_list[-2]+new_list[-3])