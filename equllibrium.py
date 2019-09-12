a=int(input())
y=[int(x) for x in input().split()]
i=len(y)
s1=0
s2=0
for l in range(i):
    s1=0
    s2=0
    for n in range(l):
        s1+=y[n]
    for d in range(l+1,i):
        s2+=y[d]
    if s1==s2:
        print(l)
        break
else:
    print(-1)
