x = [i for i in range(1, 31)]
for i in range(1, 29):
	n = int(input()) - 1
	x[n] = 0
x = sorted(x)
print(x[28], x[29], sep="\n")