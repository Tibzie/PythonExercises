
def cond1(a, b, c):
	sum = a + b
	mul = a * b

	if a==0 and b!=0:
		return b
	elif b==0 and a!=0:
		return a
	elif a==0 and b==0:
		print("Invalid numbers.")

	if c==True:
		return sum
	else:
		return mul

print (cond1(4,4,True))