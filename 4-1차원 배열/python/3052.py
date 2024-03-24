x = []
for i in range(11):
	x.append(int(input()) % 42)
a = []
c = 0
for b in x:
	if b not in a:
		c += 1
	a.append(b)
print(c)