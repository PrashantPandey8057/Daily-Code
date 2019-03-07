q=int(input())
h=int(input())
l=[]
u=[]
n=q**2
m=h**2
l.append(n)
u.append(m)
if m in l and n in u:
    print("Equal")
else:
    print("Not equal")
    
