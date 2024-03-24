x = int(input())
n = int(input())
r = 0
for i in range(0, n):
	a, b = map(int, input().split(" "))
	r += a * b
print("Yes" if x == r else "No")