a = input().split(" ")
b = [1, 1, 2, 2, 2, 8]
for i in range(len(a)):
	a[i] = str(b[i] - int(a[i]))
print(' '.join(a))