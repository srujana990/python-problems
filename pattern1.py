#3 3 3 2 2 2 1 1 1
#3 3 2 2 1 1
#3 2 1
for i in range(3,0,-1):
    for j in range(3,0,-1):
        k=i
        while k>0:
            print(j,end=' ')
            k=k-1
    print()