#input: 12
#input: 18
#output: 6
#output: 36
a = int(input())
b = int(input())
aa=a
bb=b
while b != 0:
    temp = b
    b = a % b
    a = temp
gcd=a
lcm=abs(aa*bb)//gcd
print(gcd)
print(lcm)

