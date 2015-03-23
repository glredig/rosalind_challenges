def dom_offspring():
	floats = map(float, raw_input("ints: ").rstrip().split())

	sum = 0.0

	sum += floats[0]
	sum += floats[1]
	sum += floats[2]
	sum += floats[3] * .75
	sum += floats[4] * .5

	print sum * 2 
dom_offspring()
