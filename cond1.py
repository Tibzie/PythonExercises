
def cond1(a, b, c):
	sum = a+b
	mul = a*b
	if c==True:
		return sum
	else:
		return mul

print (cond1(3,4,True))