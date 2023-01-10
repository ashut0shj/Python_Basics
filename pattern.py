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
welcome_pat()


def print_rangoli(size):
    alp=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    b = (size*4-3) // 2
    l = []
    for i in range(size):
        if i == 0:
            l.append('-' * b + alp[size-i-1] + '-' * b)
        else:
            d = l[i-1][2:b+1]+'-'+alp[size-i-1]
            l.append(d + d[-2::-1])
    l += l[-2::-1]
    print('\n'.join(l))
