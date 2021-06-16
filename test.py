dim=4
c1=[]
z=[]
for x in range(dim):
    c1.append(0)
for x in range(dim):
    z.append(c1)
print(z)
c=[]
for i in range(dim):
    c.append([])
for i in range(dim):
    for j in range(dim):
        c[i].append(0)
print(c)