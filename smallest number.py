def smallest_of_three(a, b, c):
    if a <= b and a <= c:
        return a
    elif b <= a and b <= c:
        return b
    else:
        return c
n1=int(input())
n2=int(input())
n3=int(input())
print(f"The smallest of {n1},{n2},and {n3} is \n{smallest_of_three(n1,n2,n3)}")
