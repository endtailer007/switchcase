upper=int(input("Enter a upper limit: "))
lower=int(input("Enter a lower limit: "))
for num in range(lower,upper+1):
    if num>1:#since all prime numbers are greater than one
        for i in range(2,num):
            if (num%i)==0:
                break
        else:
            print(num)
#program to check whether a given number is prime or not
p=int(input("Enter a number: "))
var=False
if p>1:
    for i in range(2,p):
        if (p%i)==0:
            var=True
            break
if var:
    print(p,"number is not a prime number")
else:
    print(p,"number is a prime number")
