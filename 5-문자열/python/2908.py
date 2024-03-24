a = input().split(" ")
b = []
for i in a:
	b.append(int(''.join(reversed(i))))
print(sorted(b)[1])