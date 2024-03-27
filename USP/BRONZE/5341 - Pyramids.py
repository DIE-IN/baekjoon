while True:
	a = int(input())
	if a == 0:
		break
	b = 0
	for i in range(a):
		b += a - i
	print(b)