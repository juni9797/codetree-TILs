n = int(input())

list = []
five_list = []
i = 1

while len(five_list)<2:
    
    list.append(n*i)
    
    if n*i % 5 == 0:
        five_list.append(n*i)
    
    i = i+1

    
print(*list)