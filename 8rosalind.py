def consensus():
	print max(1, 3, 0, 2, 3)
	filename = raw_input("File: ")
	consensus = ''
	strands = []
	strand = ''
	counts = []
	a_seq, t_seq, g_seq, c_seq = [], [], [], []
	with open(filename, "r") as f:
		for line in f:
			if line.startswith(">"):
				if strand:
					strands.append(strand)				
				strand = ''
			else: 
				strand += line.rstrip()
	strands.append(strand)
	for nt in range(len(strands[0])):
		print "Count me"
		max_num = 0
		max_ltr = ''
		a, c, t, g = 0, 0, 0, 0
		for s in range(len(strands)):
			if strands[s][nt] == 'A':
				a += 1
			elif strands[s][nt] == 'T':
				t += 1
			elif strands[s][nt] == 'G':
				g += 1
			elif strands[s][nt] == 'C':
				c += 1
	
		a_seq.append(str(a))
		t_seq.append(str(t))
		g_seq.append(str(g))
		c_seq.append(str(c))
		if max(a, c, t, g) == a:
			consensus += 'A'
		elif max(a, c, t, g) == c:
			consensus += 'C'
		elif max(a, c, t, g) == t:
			consensus += 'T'
		elif max(a, c, t, g) == g:
			consensus += 'G'
		
	print consensus
	print "A:", ' '.join(a_seq)
	print "T:", ' '.join(t_seq)
	print "G:", ' '.join(g_seq)
	print "C:", ' '.join(c_seq)
consensus()
