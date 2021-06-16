def init(dim):
    '''c=[]
    z=[]
    for x in range(dim):
        c.append(0)
    for x in range(dim):
        z.append(c)
    print(z)
    return z '''
    c=[]
    for i in range(dim):
        c.append([])
    for i in range(dim):
        for j in range(dim):
            c[i].append(0)
    return c


def dot(a,b):
    s = 0
    for i in range(len(a)):
        s = s+(a[i]*b[i])
    return s


def row(M,i):
    ith=[]
    for x in range(len(M)): #length of M works because its a square matrix
        ith.append(M[i][x])
    return ith


def column(M,j):
    jth=[]
    for y in range(len(M)):
        jth.append(M[y][j])
    return jth


def mat_multiplication(k,m):
    c = init(len(k))
#    print(c)
#    print(len(k), len(m))
    for ii in range(len(k)):
        for jj in range(len(m)):
            c[ii][jj] = dot(row(k, ii), column(m, jj))
            #print(dot(row(k, ii), column(m, jj)))
    return c


A = [[1,2,3],[4,5,6],[7,8,9]]
B = [[1,2,3],[4,5,6],[7,8,9]]
C=mat_multiplication(A,B)
print(C)