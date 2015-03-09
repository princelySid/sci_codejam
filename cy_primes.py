def is_divisible(var):
	limit = var/2
	store =[var]
	
	for number in xrange(1,limit+1):
		if var%number == 0:
			store.append(number)
	limit = len(store)
	
	sum_all= 0
	
	for x in xrange(1,limit):
		sum_all+=store[x]
	return sum_all


def testing_amicable(var):
	againgst=is_divisible(var)
	if var == is_divisible(againgst) and var!=againgst:
		return True, var, againgst
def amicable_product():
	product=1
	for x in xrange(1,10000):
		 	if testing_amicable(x) != None:
		 		amicable=testing_amicable(x)[1]
		 		print amicable
		 		product*=amicable
	return product
print amicable_product()
