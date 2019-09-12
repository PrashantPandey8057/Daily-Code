a=int(input())
h=[int(x) for x in input().split()]
i=max(h)
w=[0]*i*a
for j in h:
    w[j]+=1
n=max(w)
print(w.index(n))
