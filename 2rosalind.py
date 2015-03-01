def transcribe():
	dna = raw_input("string: ")	
	dna = list(dna)
	for i in range(len(dna)):
		if dna[i] == "T":
			dna[i] = "U"

	print "".join(dna)
	return "".join(dna)

transcribe()
