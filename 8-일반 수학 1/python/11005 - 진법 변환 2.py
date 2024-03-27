n, b = map(int, input().split(" "))
t = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
r = ""
while(n > 0):
	n, a = divmod(n, b)
	r += t[a - 10] if a > 9 else str(a)
print(''.join(reversed(r)))