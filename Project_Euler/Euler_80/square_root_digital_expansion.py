from decimal import Context, Decimal


sqrt_rat = {x**2 for x in xrange(1, 11)}
sqrt_irr = {x for x in xrange(1, 101) if x not in sqrt_rat}

def solution(dec_digits=100):
	total = 0
	acc = Context(dec_digits) # get accurancy
	for x in sqrt_irr:
		x = Decimal(x)
		sqrt_x = x.sqrt(acc)
		sum_decimals = sum(sqrt_x.as_tuple().digits[1:])
		total += sum_decimals
		print('Number: %s\nSquare root: %s\nDigits Sum: %s\nTotal: %s' % (x, sqrt_x, sum_decimals, total))
		print('***'*10)

	print total
	return total

solution()







