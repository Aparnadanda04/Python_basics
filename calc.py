#calc
def add(x,y):
    return(x + y)

def sub(x,y):
    return(x - y)

def div(x,y):
    return(x//y)

def mul(x,y):
    return(x*y)

def pow(x,y):
    return(x ** y)
n = int(input())
print("1:add,2:sub,3:div,4:mul,5:pow")


if n == 1:
    a=int(input())
    b=int(input())
    ans=add(a,b)
    print(ans)
elif n == 2:
    a=int(input())
    b=int(input())
    ans=sub(a,b)
    print(ans)
elif n == 3:
    a=int(input())
    b=int(input())
    ans=div(a,b)
    print(ans)

elif n == 4:
    a=int(input())
    b=int(input())
    ans=mul(a,b)
    print(ans)
elif n == 5:
    a=int(input())
    b=int(input())
    ans=pow(a,b)
    print(ans)

else:
    print("please enter appropriate no:")

