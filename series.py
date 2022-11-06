def fibonacci(n):
    l=[]
    i=0
    a=1
    while a<n:
        l.append(a)
        a+=l[i-1]
        i+=1
    return l
print(fibonacci(10))