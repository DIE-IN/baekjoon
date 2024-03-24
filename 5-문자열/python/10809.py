s = input()
a = "abcdefghijklmnopqrstuvwxyz"
b = []
for i in range(26):
	b.append(str(s.find(a[i])))
print(" ".join(b))