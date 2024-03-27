a = 1
while (a != 0):
	a, b = map(int, input().split(" "))
	if a == 0:
		break
	print(a + b)