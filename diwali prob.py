n=int(input())
r=int(input())
ttime=240-r
count=0
time=0
for i in range(n):
    time+=(i+1)*5
    if time>ttime:
            break
    count=count+1
print(count)