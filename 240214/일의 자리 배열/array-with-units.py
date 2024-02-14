fibo = list(map(int, input().split()))

for i in range(2,10):
    if fibo[-1]+fibo[-2] < 10:
        fibo.append(fibo[-1]+fibo[-2])
    else:
        fibo.append(fibo[-1]+fibo[-2]-10)
        
print(*fibo)