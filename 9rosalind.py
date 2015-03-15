def hamming():
	dna_1 = raw_input("Enter string 1: ")
	dna_2 = raw_input("Enter string 2: ")

	d_h = 0

	for i in range(len(dna_1)):
		if dna_1[i] != dna_2[i]:
			d_h += 1

	print d_h

hamming()
