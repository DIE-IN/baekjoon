a = int(input())
b = int(input())
c = int(input())
r = str(a*b*c)
print(r.count("0"))
for i in range(1, 10):
	print(r.count(str(i)))