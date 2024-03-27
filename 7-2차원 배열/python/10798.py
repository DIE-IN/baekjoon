# 세로읽기

a = [[]for i in range(15)]
l = 0
for i in range(5):
	b = input()
	l = len(b)
	for x in range(l):
		a[x].append(b[x])
c = ''
for i in a:
	c += ''.join(i)
print(c)