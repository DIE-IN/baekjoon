l = input()
a = l[0:][:round(len(l)/2 - 0.1)]
b = list(l[round(len(l)/2 - 0.1):])
if len(l) % 2 != 0:
	b.pop(0)
print(1 if a == ''.join(reversed(b)) else 0)