n=5
l=1
for i in range(n):
    for j in range(0,l):
        print('*',end=' ')
    print()
    l+=1
k=5

for i in range(n-1):
    for j in range(1,k):
        print('*',end=" ")
        
    k-=1
    print()