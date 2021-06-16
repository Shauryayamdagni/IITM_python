
n=int(input())
mat=[]
for i in range(n):
    mat.append([])
for i in range(n):
    for j in range(n):
        mat[i].append(int(input()))
print(mat)