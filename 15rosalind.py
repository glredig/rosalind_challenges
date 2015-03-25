import fasta

def shared_motif():
	filename = raw_input("File: ")

	max_string = ''
	current_string = ''

	pairs = fasta.read_fasta_from_file(filename)
	current_string = pairs[0][1][1]

	def find_max_motif(motif):
		common = True
		for j in xrange(1, len(pairs) - 1):
			if motif in pairs[j][1]:
				print motif
			else:
				common = False
		return common

	for i in xrange(len(pairs[0][1]) - 1):
		diff = 1
		while find_max_motif(current_string) and (i + diff < len(pairs[0][1])):
			if len(current_string) > len(max_string):
				max_string = current_string
			
			if len(pairs[0][1]) > (i + diff):
				current_string += pairs[0][1][i + diff]
				print "added to string"
			diff += 1
		else:
			 current_string = ''

		print max_string
		print current_string	
		print pairs[0][1][i]

	print "Max string: %s" % max_string

shared_motif()
