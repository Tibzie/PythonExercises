def cond1(list, c):
	sum = 0
	mul = 1
	if c==True:
		for i in list:
			sum = sum + i
		return sum
	else:
		for j in list:
			mul = mul * j	
		return mul

print (cond1([1,2,3,4,5,6,7,8,9,10], True))
