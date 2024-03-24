n, m = input().split(" ")
n = int(n); m = int(m)
a = ["0" for i in range(1, n+1)]
for i in range(0, m):
	i, j, k = map(int, input().split(" "))
	for e in range(i-1, j):
		a[e] = str(k)
print(" ".join(a))