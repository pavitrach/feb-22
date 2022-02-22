n=int(input())
for i in range(1,n+1):
    for j in range(n,0,-1):
        if i>=j:
            print("* ",end="")
        else:
            print(" ",end="")
    print("\n")

for k in range(n,1,-1):
    for m in range(n,1,-1):
        if k>=m:
            print(" *",end="")
        else:
            print(" ",end="")
    print("\n")
