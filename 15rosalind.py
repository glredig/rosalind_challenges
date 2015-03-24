import fasta

def shared_motif():
	filename = raw_input("File: ")

	max_string = ''
	current_string = ''

	pairs = fasta.read_fasta_from_file(filename)
	max_string, current_string = pairs[0][1]
	for i in xrange(len(pairs[0][1]) - 1):
		while find_max_motif(current_string):
			if len(current_string) > max_string:
				max_string = current_string
			
			if len(pairs[0][1]) > (i + 1):
				current_string += pairs[0][1][i + 1]
		else:
			 current_string = ''

		print max_string
		print current_string	
		print pairs[0][1][i]

find_max_motif(motif):
	common = True
	for j in xrange(1, len(pairs) - 1):
		if motif in pairs[j][1]:
			print motif
		else:
			common = False
	return common


shared_motif()
