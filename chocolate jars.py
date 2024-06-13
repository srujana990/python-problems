c=list(map(int,input().split()))
n=int(input())
a=0
for i in c:
    print('this iteration is for',i)
    a=a+i//3
    print(a)
    if i%3!=0:
        a=a+1
    else:
        a=a+0
print(a)



