a, b = map(int, input().split(" "))
if b - 45 >= 0:
	print(a,b-45)
else:
	b = 60 + (b - 45)
	c = a - 1
	if a == 0:
		c = 23
	print(c, b)