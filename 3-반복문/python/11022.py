for i in range(1, int(input())+1):
	a, b = input().split(" ")
	i = str(i); a = int(a); b = int(b)
	print("Case #{}: {} + {} = {}".format(i, a, b, str(a+b)))