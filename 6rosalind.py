def motif():
	dna_term = raw_input("Please enter the search term:")
	dna_content = raw_input("Please enter the entire content:")
	match_sites = []

	for i in range(len(dna_content)):
		for j in range(len(dna_term)):
			if (i + j < len(dna_content)) and dna_term[j] == dna_content[i + j]:
				if j == len(dna_term) - 1:
					match_sites.append(i)
			else:
				break

		
	for site in match_sites:
		print site + 1


motif()
