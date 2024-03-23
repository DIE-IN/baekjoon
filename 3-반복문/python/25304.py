x=int(input())
n=int(input())
r=0
for i in range(0, n):
	a, b = input().split(" ")
	r += int(a) * int(b)
print("Yes" if x==r else "No")