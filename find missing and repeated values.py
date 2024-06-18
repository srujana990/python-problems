#find missing number and repeated number in the given array
#input[[1,3],[2,2]]
#output[2,4]
a=[]
for i in range(0,3):
    sub=[]
    print('enter values for row',i)
    for j in range(0,3):
        print('enter values for coloumn')
        ele=int(input())
        sub.append(ele)
        print(sub)
    a.append(sub)
    print(a)
d={}
ans=[]
r=0
c=0
for i in range(0,r):
    for i in range(0,c):
        if a[i][j] not in d:
            d[a[i][j]]=1
        else:
            d[a[i][j]]+=1
            if d[a[i][j]]==2:
                ans.append(a[i][j])
print(d)
for i in range(1,r**2+1):
    if i not in d:
        ans.append(i)
print(d)
print(ans)

