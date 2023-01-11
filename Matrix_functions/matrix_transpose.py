#transpose of 3x3 matrix
def transpose(m):
    t=[[],[],[]]
    for i in m:
        a=0
        for j in i:
            t[a].append(j)
            a+=1
    return t
