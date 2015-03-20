def consensus():
	filename = raw_input("File: ")
	consensus = ''
	strands = []
	strand = ''
	counts = []

	with open(filename, "r") as f:
		for line in f.read():
			if line.startswith(">"):
				if strand:
					strands.append(strand)				
				strand = ''
			else:
				strand += line.rstrip()

	for nt in range(len(strands[0] - 1):
		max_num = 0
		max_ltr = ''
		a, c, t, g = 0, 0, 0, 0

		for seq in strands:
			if strands[seq][nt] == 'A':
				a += 1
			elif strands[seq][nt] == 'T':
				t += 1
			elif strands[seq][nt] == 'G':
				g += 1
			elif strands[seq][nt] == 'C':
				c += 1
		




consensus():
