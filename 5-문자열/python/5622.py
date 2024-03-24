s = input()
a = 0
for i in range(len(s)):
	n = s[i]
	b = round(ord(n) / 3 - 19)
	if n == "S" or n == "V" or b == 11:
		b -= 1
	a += b
print(a)