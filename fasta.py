def read_fasta_from_file(filename):
	dna_tuples = []
	ids = []
	strands = []
	strand = ''
	with open(filename, 'r') as openFile:
		for line in openFile:
			if line.startswith('>'):
				ids.append(line[1:].rstrip())
				if strand:
					strands.append(strand)
				strand = ''
			else:
				strand += line.rstrip()

		strands.append(strand)

	return zip(ids, strands)		


