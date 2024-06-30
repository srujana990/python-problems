#input: aaabbbccdddd
# output: 8
s=input()
d={}
max=-999
for i in s:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
    if d[i]>max:
            max=d[i]
print(len(s)-max)

