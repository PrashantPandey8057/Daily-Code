#1-Character PAttern
n=int(input())
t=65
for j in range(1,n+1):
    for c in range(j):
        print(chr(t),end='')
    t+=1
    print()


#2-Binary PAttern
f=int(input())
o=0
for j in range(f,0,-1):
    o+=1
    for k in range(1,j+1):
        if o%2==0:
            print("0",end='')
        else:
            print("1",end='')
    print()
 
