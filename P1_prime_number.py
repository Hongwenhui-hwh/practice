i = 1
for i in range(1,100):
      j = 1
      for j in range(1,100):
        if((j<i)&(i%j==0)&(j!=1)):
              break
        elif(i==j):
            print(i)
