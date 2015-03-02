def recurrence():
	"""Comma separated assignment evaluates right side before assigning"""
	multiplier = int(raw_input("Enter the multiplier (k): "))
	term = int(raw_input("Enter the term which you wish to calculate: "))

	a = 1
	b = 1

	for i in range(2, term):
		a, b = b, a*multiplier + b
	
	print b

recurrence()
	
