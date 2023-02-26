#welcome footmat

def rangoli():
    n=int(input("Enter the size of rangoli : "))
    alp=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    b = (n*4-3) // 2
    l = []
    for i in range(n):
        if i == 0:
            l.append('-' * b + alp[n-i-1] + '-' * b)
        else:
            d = l[i-1][2:b+1]+'-'+alp[n-i-1]
            l.append(d + d[-2::-1])
    l += l[-2::-1]
    print('\n'.join(l))
