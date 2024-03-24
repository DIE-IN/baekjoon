l = input()
a = 'c=,c-,dz=,d-,lj,nj,s=,z='.split(",")
for i in a:
	l = l.replace(i, ' ')
print(len(l))