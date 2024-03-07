n = int(input())

list = list(map(int, input().split()))

cnt_list = [0]*10

for i in list:
    cnt_list[i] += 1

for i in range(1, 10):
    print(cnt_list[i])