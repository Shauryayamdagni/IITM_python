def min_dict_key(data):
    min=10000000000000
    for x in data.keys():
        if x<min:
            min=x
    return min


def max_dict_key(data):
    max=0
    for x in data.keys():
        if x >max:
            max=x
    return max


def min_value_dict_key(data):
    min=1000000000
    i=0
    for x in data.keys():
        if data[x] < min:
            min =data[x]
            i=x
    return i


def max_value_dict_key(data):
    max=-10000000000
    i=0
    for x in data.keys():
        if data[x] > max:
            max=data[x]
            i=x
    return i


def sort_by_key(data, order="asc"):
    temp=()
    l=[]
    for x in data.keys():
        temp=(x,data[x])
        l.append(temp)
    if order == "asc":
        for x in range(len(l)):
            min = l[x][0]
            i=x
            for y in range(x+1,len(l)):
                if min > l[y][0] :
                    min=l[y][0]
                    i=y
            l[x],l[i]=l[i],l[x]
        return l
    if order == "desc":
        for x in range(len(l)):
            min = l[x][0]
            i=x
            for y in range(x+1,len(l)):
                if min < l[y][0] :
                    min=l[y][0]
                    i=y
            l[x],l[i]=l[i],l[x]
        return l


def sort_by_value(data, order="asc"):
    temp = ()
    l = []
    for x in data.keys():
        temp = (x, data[x])
        l.append(temp)
    if order == "asc":
        for x in range(len(l)):
            min = l[x][1]
            i = x
            for y in range(x + 1, len(l)):
                if min > l[y][1]:
                    min = l[y][1]
                    i = y
            l[x], l[i] = l[i], l[x]
        return l
    if order == "desc":
        for x in range(len(l)):
            min = l[x][1]
            i = x
            for y in range(x + 1, len(l)):
                if min < l[y][1]:
                    min = l[y][1]
                    i = y
            l[x], l[i] = l[i], l[x]
        return l