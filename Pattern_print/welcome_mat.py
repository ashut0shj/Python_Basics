#welcome footmat

def welcome_pat():
    #N=input().split()
    #n,m=int(N[0]),int(N[1])
    n=(int(input("enter the size : ")))
    m=n*3
    x=(n-1)//2
    for i in range (x):
        r=(i*2)+1
        t=((m)//2)-((r*3)//2)
        print(("-"*t)+ r*".|." + ("-"*t))
    l=(m-7)//2
    print(("-"*l)+"WELCOME"+("-"*l))
    for ii in range (x):
        i=x-ii-1
        r=(i*2)+1
        t=((m)//2)-((r*3)//2)
        print(("-"*t)+ r*".|." + ("-"*t))
welcome_pat()   #calling
