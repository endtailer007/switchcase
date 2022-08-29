def rat_food(r,unit,arr,n):
    if n==0:
        return -1
    tf=r*unit
    initial_food=0
    for i in range(n):
        initial_food+=arr[i]
        if initial_food>=tf:
            break
    if tf>initial_food:
        return 0
    return i+1


r=int(input("Enter the number of rats: "))
unit=int(input("Enter the number of food quantity each rat consumes: "))
n=int(input("Enter the size of the array: "))
arr=list(map(int,input().split()))
food=rat_food(r,unit,arr,n)
print(food)
