s=input()
v="aeiou"
d={}
ans=0
max=-999
for i in s:
        if i not in d:
            d[i]=1
        else:
            d[i]+=1
        if d[i]>max:
            max=d[i]
            ans=i
print(d)
print(ans)



