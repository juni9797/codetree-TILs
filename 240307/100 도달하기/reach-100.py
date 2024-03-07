n = int(input())

list = [1]
a = 1
b = n

while list[-1] < 100:
    a,b = b, a+b
    list.append(a)

print(*list)