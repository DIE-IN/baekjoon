p = [[0 for x in range(100)] for x in range(100)]
for i in range(int(input())):
	a, b = map(int, input().split(" "))
	for c in range(a, a+10):
		for f in range(b, b+10):
			p[c][f] = 1
d = 0
for i in range(100):
	for x in range(100):
		d += p[i][x]
print(d)