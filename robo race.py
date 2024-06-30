#input: 2 3 1 4
#output: 5
x,n,y,m=list(map(int,input().split()))
time=max(x,y)
while True:
    if time>x and (time-x)%n==0 and time>y and (time-y)%m==0:
        print(time)
        break
    time+=1