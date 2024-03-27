# 행렬 덧셈

n, m = map(int, input().split(" "))
a, b, c = [],[],[]
for i in range(n * 2):
	d = input()
	a.append(d.split(" ")) if len(a) < n else b.append(d.split(" "))
for i in range(n):
	for d in range(m):
		c.append(str(int(a[i][d]) + int(b[i][d])))
for i in range(n):
	f = []
	for e in range(m):
		f.append(c[e + m*i])
	print(" ".join(f))