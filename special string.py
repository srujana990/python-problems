#input: abcd
#input: xyz
#output: 86 
ss=input()
ss1=input()
total_sum=0
m=999
for i in range(len(ss)):
    for j in range(len(ss1)):
        ascii1=ord(ss[i])
        ascii2=ord(ss1[j])
        diff=abs(ascii1-ascii2)
        if diff<m:
            m=diff
            total_sum+=diff
print(total_sum)



