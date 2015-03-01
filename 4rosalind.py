def recurrence():
	multiplier = int(raw_input("Enter the multiplier (k): "))
	term = int(raw_input("Enter the term which you wish to calculate: "))

	term -= 2

	immature = 0
	mature = 1
	current = 1

	for i in range(term):
		current += mature * multiplier 
		mature += immature
		immature = current - mature
	
	print current

recurrence()
	
