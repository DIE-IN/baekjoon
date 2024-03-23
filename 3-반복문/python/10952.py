a = ""
while (a != 0):
	a, b = input().split(" ")
	a = int(a); b = int(b)
	if a == 0:
		break
	print(a + b)