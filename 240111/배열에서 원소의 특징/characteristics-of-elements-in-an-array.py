_list = list(map(int, input().split()))

for i in range(0, len(_list)):
    if _list[i] % 3 == 0:
        print(_list[i-1])
        break