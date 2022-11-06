def fibonacci(n):
    #n=range for fib function, function will return a fibonacci in a list
    l=[]
    i=0
    a=1
    while a<n:
        l.append(a)
        a+=l[i-1]
        i+=1
    return l
