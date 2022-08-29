def recurfib(n):
    if n<=1:
        return n
    else:
        return(recurfib(n-1)+recurfib(n-2))


nterms=int(input("Enter the range of fibonacci series: "))
if nterms<=0:
    print("Please enter a positive number: ")
else:
    print("Fibonacci series is: ")
    for i in range(nterms):
        print(recurfib(i),end=" ")


