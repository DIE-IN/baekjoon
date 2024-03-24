a, b, c = map(int, input().split(" "))
if a == b == c:
	d = 10000 + a * 1000
elif a == b or a == c:
	d = 1000 + a * 100
elif b == c:
	d = 1000 + b * 100
else:
	d = a * 100 if a > b and a > c else (b * 100 if b > a and b > c else c * 100)
print(d)