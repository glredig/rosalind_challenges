def count_nucleotides():
	dna = raw_input("string: ")
	a = 0
	c = 0
	g = 0
	t = 0
	for i in dna:
		if i == "A":
			a += 1
		elif i == "C":
			c += 1
		elif i == "G":
			g += 1
		elif i == "T":
			t += 1
		else:
			print "Invalid value: %s" % i
       
	print "%s %s %s %s" % (a, c, g, t)
	return a, c, g, t

count_nucleotides()

