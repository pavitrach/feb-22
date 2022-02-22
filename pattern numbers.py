n=int(input())
for k in range (1,n+1):
    for m in range (1,k+1):
        print(m,end="")
    print("\n")
for i in range (1,n+1):
    for j in range (1,n-i+1):
        print(j,end="")
    print("\n")
