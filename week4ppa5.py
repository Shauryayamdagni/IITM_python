s=str(input())
l=s.split(",")
for x in range(0, len(l)-1):
    for y in range(x+1, len(l)):
        if l[y] != l[x]:
            continue
        l.pop(y)
for y in range(0, len(l)):
    if y!=(len(l)-1):
        print(l[y],end=',')
    else:
        print(l[y])