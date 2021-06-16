def column(tab):
    d={}
    l=[]
    k=[]
    temp={}
    for x in range(0, len(tab)):
        m=list(tab[x].keys())
        k.append(m[0])
    n=len(tab[0][k[0]])
    for x in range(0,n):
        i=0
        for y in k:
            temp[y]=tab[i][y][x]
            i=i+1
        l.append(dict(temp))
        temp={}
    return l


tab=[{'roll':[1,2,3]},{"name":['sudarshan','shaurya', 'angel']},{'course':['x','y','z']}]
print(column(tab))