def mortal_rabbit():
	n = int(raw_input("Enter months (n): "))
	m = int(raw_input("Enter lifespan (m): "))

	tracker = [1, 1]
	def fib(i, j):
		v = 2
		while v < i:
			
			if v < j:
				print "v < j"
				tracker.append(tracker[-2] + tracker[-1])
			elif v == j or v == j + 1:
				print "="
				tracker.append(tracker[-2] + tracker[-1] - 1)
			else:
				print tracker
				tracker.append(tracker[-2] + tracker[-1] - tracker[-(j + 1)])
	
			v += 1
	fib(n, m)
	print tracker[-1]
mortal_rabbit()
