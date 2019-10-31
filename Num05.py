i = 2
flag = 0
while True:
    for x in range(1, 17):
        if i % x == 0:
            x = x + 1
            flag = 1
        else:
            flag = 0
            break
    if flag == 1:
        print(i)
        break
    i = i+1
