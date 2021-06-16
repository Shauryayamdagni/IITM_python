def solve(a, b):
    sol=[0,0,0]
    for i in range(3):
        a[i]=int(a[i])
        b[i]=int(b[i])
    #a[2]=(0-a[2])
    #b[2]=(0-b[2])
    #print(a,b)
    sol[0]=(a[1]*b[2])-(a[2]*b[1])
    sol[1]=(a[2]*b[0])-(b[2]*a[0])
    sol[2]=(b[1]*a[0])-(a[1]*b[0])
    #print(sol)
    final=[0,0]
    final[0]=int((sol[0]/sol[2]))
    final[1]=int((sol[1]/sol[2]))
    print(final)
    return None



#for i in range(0,3):
a=str(input())
#for i in range(0,3):
b=str(input())
a=a.split(' ')
b=b.split(" ")

solve(a,b)