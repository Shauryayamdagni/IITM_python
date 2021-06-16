#sum of series from 1 to n
def add(n):
    if(n==1):
        return 1
    else:
        return(n+add(n-1))


def compound(P,r,t):
    if(t == 1):
        return P*((r/100)+1)
    else:
        P = P*((r/100)+1)
        t=t-1
        return(compound(P,r,t))



def fact(n):
    if n==0:
        return 1
    else:
        return (n*fact(n-1))



P=int(input("enter the effing number !!"))
#r=int(input("enter the effing number !!"))
#n=int(input("enter the effing number !!"))
print(fact(P))