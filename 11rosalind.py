def rna_to_protein():
	file = open("ros2.txt", "r")
	rna = file.read().rstrip()
	protein = ''
	i = 0
	while i < len(rna) - 1:
		print "Blah"
		codon = ''
		for k in range(3):
			print "K"
			if i + k < len(rna) - 1:
				codon += rna[i + k]
		if return_protein(codon):
			protein += return_protein(codon)
		else:
			break
		i += 3
	print protein 

	file.close()

def return_protein(codon):
	print "Prot"
	if codon == "UUU" or codon == "UUC":
		return "F"
	elif codon == "UUA" or codon == "UUG":
		return "L"
	elif codon == "UCU" or codon == "UCC" or codon == "UCA" or codon == "UCG":
		return "S"
	elif codon == "UAU" or codon == "UAC":
		return "Y"
	elif codon == "UGU" or codon == "UGC":
		return "C"
	elif codon == "UGG":
		return "W"
	elif codon == "CUU" or codon == "CUC" or codon == "CUA" or codon == "CUG":
		return "L"
	elif codon == "CCU" or codon == "CCC" or codon == "CCA" or codon == "CCG":
		return "P"
	elif codon == "CAU" or codon == "CAC":
		return "H"
	elif codon == "CAA" or codon == "CAG":
		return "Q"
	elif codon == "CGU" or codon == "CGC" or codon == "CGA" or codon == "CGG":
		return "R"
	elif codon == "AUU" or codon == "AUC" or codon == "AUA":
		return "I"
	elif codon == "AUG":
		return "M"
	elif codon == "ACU" or codon == "ACC" or codon == "ACA" or codon == "ACG":
		return "T"
	elif codon == "AAU" or codon == "AAC":
		return "N"
	elif codon == "AAA" or codon == "AAG":
		return "K"
	elif codon == "AGU" or codon == "AGC":
		return "S"
	elif codon == "AGA" or codon == "AGG":
		return "R"
	elif codon == "GUU" or codon == "GUC" or codon == "GUA" or codon == "GUG":
		return "V"
	elif codon == "GCU" or codon == "GCC" or codon == "GCA" or codon == "GCG":
		return "A"
	elif codon == "GAU" or codon == "GAC":
		return "D"
	elif codon == "GAA" or codon == "GAG":
		return "E"
	elif codon == "GGU" or codon == "GGC" or codon == "GGA" or codon == "GGG":
		return "G"
	else:
		return False

rna_to_protein()
