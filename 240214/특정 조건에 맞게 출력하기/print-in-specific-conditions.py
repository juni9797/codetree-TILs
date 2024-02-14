list = list(map(int, input().split()))

zero = list.index(0)

new_list = list[0:zero]

result = []

for i in new_list:
    if i%2 == 0:
        result.append(i//2)
    else:
        result.append(i+3)

print(*result)