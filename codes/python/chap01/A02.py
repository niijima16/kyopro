x,y = map(int, input().split())
a = list(map(int, input().split()))
ans = False

for i in range(x):
    if a[i] == y:
        ans = True

if ans == True:
    print("Yes")
else:    
    print("No")
