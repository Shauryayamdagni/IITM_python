n=int(input("enter the dimension"))
l1=[]
zero=[]
s=[]
a=[]
b=[]
for x in range(0,n):
    for y in range(0,n):
        num=int(input())
        l1.append(num)
    a.append(l1)
    l1=[]
for x in range(0,n):
    for y in range(0,n):
        num=int(input())
        l1.append(num)
        zero.append(0)
    b.append(l1)
    s.append(zero)
    zero=[]
    l1=[]
#print(s)
for i in range(0,n):
    for j in range(0,n):
        s[i][j]=a[i][j]+b[i][j]
print(a)
print(b)
print(s)