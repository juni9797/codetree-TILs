list = list(map(int, input().split()))

a = list[0]
b = list[1]

for i in range(8):
    a,b = b, 2*a+b
    list.append(b)
    
print(*list)