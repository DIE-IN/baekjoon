n = int(input())
c = 0
d = []
for i in range(n):
	a = input()
	l = []
	for b in a:
		if b in l:
			if l[len(l)-1] == b:
				l.append(b)
			else:
				l[0] = "!"
		else:
			l.append(b)
	if l[0] != "!":
		d.append(l)
print(len(d))