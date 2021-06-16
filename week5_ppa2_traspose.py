def personalprint(arr1):
    for i in range(len(arr1)):
        print(arr1[i],end=" ")
    print()


def transpose(arr,i,j):
    arr1=[]
    for x in range(j):
        for y in range(i):
            arr1.append(arr[y][x])
        personalprint(arr1)
        arr1=[]
    return None


f=str(input())
f=f.split(" ")
i=int(f[0])
j=int(f[1])
arr=[]
for x in range(i):
    s=str(input())
    s=s.split(" ")
    arr.append(s)
transpose(arr,i,j)
#print(arr)