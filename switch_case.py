#Program to swap two numbers
a=int(input("Please enter the number: "))
b=int(input("Please enter the number: "))
#With temporary variable
temp=a
a=b
b=temp
#Without temporary variable
a,b=b,a
print("a=",a,"b=",b)