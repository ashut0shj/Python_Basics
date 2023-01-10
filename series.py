
def fibonacci(n):
    l=[]
    i=0
    a=1
    while a<n:
        l.append(a)
        a+=l[i-1]
        i+=1
    return l

#prints a welcome pattern
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

#checks whether a number is palindrome or not
def pal(n):
    n=str(n)
    l=int(len(str(n)))
    for i in range ((l//2)):
        p=0
        if n[i]!=n[l-i-1]:
            res=False
            break
        else:
            res=True
    return res
    


#returns the sum of series of multiples upto a number
def sumseries(n,d):
    nd=(n//d)
    return (nd/2)*(nd+1)*d


def bubbleSort(arr):
    n = len(arr)
    swapped = False
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j + 1]:
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        if not swapped:
            return


#to find transpose of a 3x3matrix 
def transpose(m):
    t=[[],[],[]]
    for i in m:
        a=0
        for j in i:
            t[a].append(j)
            a+=1
    return t


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

