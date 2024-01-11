num_list = list(map(int, input().split()))

even_list = []
three_list = []

for i in range(0, 10):
    if i % 2 != 0:
        even_list.append(num_list[i])
    if i % 3 == 2:
        three_list.append(num_list[i])

print(sum(even_list), end = ' ')
print(sum(three_list)/len(three_list))