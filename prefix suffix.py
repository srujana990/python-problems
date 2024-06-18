#input: 5
#input: 1 2 3 4 5
#output:[13,9,3,5,15]
n=int(input())
a=list(map(int,input().split()))
ts=0
rs=0
ls=0
cs=0
ans=[]
for i in a:
    ts+=i
for i in a:
    ls+=i
    rs=ts-ls
    cs=abs(rs-ls)
    ans.append(cs)
print(ans)



