t = int(input())
a = ""
for i in range(t):
	r, s = input().split(" ")
	for x in range(len(s)):
		a += s[x] * int(r)
	if i + 1 < t:
		a += "\n"
print(a)