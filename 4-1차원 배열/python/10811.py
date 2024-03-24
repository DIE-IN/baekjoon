n, m = map(int, input().split(" "))
a = [str(i) for i in range(1, n+1)]
for i in range(m):
	b, c = map(int, input().split(" "))
	d = []
	for e in range(b - 1, c):
		d.append(a[e])
	d.reverse()
	for f in range(len(d)):
		a[b - 1 + f] = d[f]
print(" ".join(a))