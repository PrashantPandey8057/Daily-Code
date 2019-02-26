a=input()
a=list(a)
x,y=0,0
for i in a:
    if i=="L":
        x=x-1
    elif i=="R":
        x=x+1
    elif i=="U":
        y=y+1
    elif i=="D":
        y=y-1
    else:
        pass
print(x,y)
f=open("a.txt","w")

