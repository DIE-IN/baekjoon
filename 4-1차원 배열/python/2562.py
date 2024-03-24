a=[]
for i in range(10):
	a.append(input())
b = sorted(a, key=lambda c: int(c))[8]
print(b, a.index(b) + 1, sep="\n")