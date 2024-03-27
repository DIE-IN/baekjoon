a = input().split(" ")
b = 0
for i in a:
	c = int(i)
	b += c * c
print(b % 10)