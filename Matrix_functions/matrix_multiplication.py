#multiplication of two 3x3 matrix
print("Enter the first matrix")
r1=input().split()
r2=input().split()
r3=input().split()
m1=[r1,r2,r3]

print("Enter the second matrix")
r1=input().split()
r2=input().split()
r3=input().split()
m2=[r1,r2,r3]

m3=[[],[],[]]
e=0
c=0

for i in range(len(m1)):
    for j in range(len(m2[0])):
        for k in range(len(m2)):
            e += int(m1[i][k]) * int(m2[k][j])
        
        m3[i].append(e)
        e=0
        


print("m1 * m2 = ")
for i in m3:
    print(i)
