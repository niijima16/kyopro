n = int(input())

for i in range(9, -1, -1):
    print(n >> i & 1, end="")