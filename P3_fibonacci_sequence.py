#     Generate the first 20 numbers of the Fibonacci sequence
def fbnq_se():
    fbnq = [0 for i in range(20)]
    for i in range(0,20):
        if i<2:
            fbnq[i] = 1
        else:
            fbnq[i] = fbnq[i-1] + fbnq[i-2]
            print(fbnq[i])
    return 

if __name__ == '__main__':
    fbnq_se()
