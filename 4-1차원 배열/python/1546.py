n = int(input())
l = list(map(int, input().split(" ")))
s = []
for i in range(n):
	s.append(l[i])
m = sorted(s)[n-1]
a = 0
for i in s:
	a += i / m * 100
print(round(a/n, 6))