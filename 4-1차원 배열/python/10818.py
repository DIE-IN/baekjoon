n = int(input())
a = input().split(" ")
b = sorted(a, key=lambda c: int(c))
print(b[0], b[n-1])