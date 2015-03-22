import fasta

def overlap():
	filename = raw_input("File: ")
	k = int(raw_input("k: "))
	
	pairs = fasta.read_fasta_from_file(filename)	

	def compare_overlap(str1, str2):	
		if str1[0] != str2[0]:
			"""if str1[1].endswith(str1[1][0:k:]) and str2[1].startswith(str1[1][-k::]):
				print "%s %s" % (str2[0], str1[0])
				print "%s %s" % (str1[0], str2[0])
			"""
			if str2[1].endswith(str1[1][0:k:]):
				print "%s %s" % (str2[0], str1[0])
			if str2[1].startswith(str1[1][-k::]):
				print "%s %s" % (str1[0], str2[0])

	for i in xrange(len(pairs)):
		for j in xrange(i, len(pairs)):
			if i != j:
				compare_overlap(pairs[i], pairs[j])
		
overlap()
