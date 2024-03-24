n = int(input())
for i in range(2 * n - 1):
	a = " " * (n - 1 - i) if i < n else " " * (i - n + 1)
	b = "*" * (i * 2 + 1) if i < n else "*" * round((n * 2 - i - 1) * 2 - 1)
	print(a + b)