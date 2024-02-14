n = int(input())
list = list(map(int, input().split()))

even_list = [i for i in list if i%2 == 0]

print(*even_list)