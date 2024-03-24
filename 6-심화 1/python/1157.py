a = input().upper()
b = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
c = ['', 0]
for i in b:
	d = a.count(i)
	if d > c[1] and c[0] != i:
		a = a.replace(i, "")
		c[0] = i
		c[1] = d
	elif d == c[1]:
		c[0] = "?"
print(c[0])