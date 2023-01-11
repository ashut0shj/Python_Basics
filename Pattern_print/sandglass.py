n=int(input("Enter number of rows : "))
for i in range (n):
    print(" "*i,end="")
    print(" *"*(n-i))
for i in range (n+1):
    print(" "*(n-i),end="")
    print(" *"*i)
