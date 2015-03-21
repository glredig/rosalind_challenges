def overlap():
	filename = raw_input("File: ")
	k = int(raw_input("k: "))
	ids = []
	strings = []	
	strand = ''

	with open(filename, 'r') as openFile:
		for line in openFile.readlines():
			if line.startswith(">"):
				ids.append(line[1:].rstrip())
				if strand:
					strings.append(strand)
					strand = ''
			else:
				strand += line.rstrip()	
		strings.append(strand)	
	
	pairs = zip(ids, strings)	

	def compare_overlap(str1, str2):
		if str1[0] != str2[0] and (str1[1][0:k:] == str2[1][-k::] or str1[1][-k::] == str2[1][0:k:]):
			print "%s %s" % (str1[0], str2[0])

	for i in xrange(len(pairs)):
		for j in range(i, len(pairs)):
			compare_overlap(pairs[i], pairs[j])
		
overlap()
