i = 1
for i in range(1, 10000):
    j = 1
    x = 0
    for j in range(1, i):
        if (j!=i)&(i%j==0):
            x = x + j
            if x==i:
                print(x, '是完美数')
                break
