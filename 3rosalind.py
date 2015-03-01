def reverse_complement():
	dna = raw_input("String: ")

	dna = list(dna)

	dna = reversed(dna)
	print dna
	for i in range(len(dna)):
		if dna[i] == "A":
			dna[i] = "T"
		elif dna[i] == "T":
			dna[i] = "A"
		elif dna[i] == "G":
			dna[i] = "C"
		elif dna[i] == "C":
			dna[i] = "G"
		else:
			print "Invalid character"

	print "".join(dna)

reverse_complement()
