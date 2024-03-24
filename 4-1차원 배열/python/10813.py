n, m = input(). split(" ")
n = int(n); m = int(m)
a = [str(i) for i in range(1, n + 1)]
for x in range(0, m):
	i, j = input().split(" ")
	i = int(i) - 1; j = int(j) - 1
	b = a[i]
	a[i] = a[j]
	a[j] = b
print(" ".join(a))