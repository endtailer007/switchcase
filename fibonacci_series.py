#program to print fibonacci series
nterms=int(input("Enter the number of terms: "))
n1,n2=0,1 #first terms
count=0
if nterms<=0:
    print("Please enter a positive number: ")
elif nterms==1:
    print("The fibonacci series upto",nterms,"is : ")
    print(n1)
else:
    print("Fibonacci sequence: ")
    while count<nterms:
        print(n1,end=" ")
        nth=n1+n2
        #update values
        n1=n2
        n2=nth
        count+=1
#program to return sum of fibonacci series
nterms=int(input("\nEnter the number of terms: "))
n1,n2=0,1
count=0
sum=0
if nterms<=0:
    print("Please enter a positive value: ")
elif nterms==1:
    print("The sum of fibonacci series upto",nterms,"is:")
    print(n1)
else:
    for i in range(0,nterms):
        sum=sum+n1
        next=n1+n2
        n1=n2
        n2=next
    print("The sum of fibonacci series upto",nterms,"is : ",sum)
