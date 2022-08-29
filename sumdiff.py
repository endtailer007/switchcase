def diffOfSum(n,m):
    nd=0
    d=0
    if n<0 or m<0:
        return 0
    else:
        for i in range(m+1):
            if i%n==0:
                d+=i
            else:
                nd+=i
    return abs(nd-d)
n=int(input())
m=int(input())
print(diffOfSum(n,m))