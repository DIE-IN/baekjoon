a, b = input().split(" ")
a = int(a); b = int(b); c = int(input())
d = b + c
if d < 60:
	print(a, d)
else:
	a += d / 60
	if a >= 24:
		a -= 24
	print(int(a), d % 60)