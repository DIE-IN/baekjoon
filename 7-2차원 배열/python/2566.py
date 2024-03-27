# 최댓값

a = ''
for i in range(9):
	a += ' '.join(input().split(" ")) + " "
a = a.split(" ")
b = []
for i in a:
	b.append(i)
b.pop(len(b) - 1)
for i in b:
	b[b.index(i)] = int(i)
m = sorted(b)[len(b)-1]
l = a.index(str(m)) + 1
p = 0
p = b.index(m) // 9 + 1
l = b.index(m) % 9 + 1
print(m)
print(round(p), l)