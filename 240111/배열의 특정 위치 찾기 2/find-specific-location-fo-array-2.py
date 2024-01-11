num = list(map(int, input().split()))

even_num = num[::2]

for i in range(0, len(even_num)):
    num.remove(even_num[i])

odd_list = num

even_sum = sum(even_num)
odd_sum = sum(odd_list)

if even_sum > odd_sum:
    result = even_sum - odd_sum
else:
    result = odd_sum - even_sum

print(result)