import re

def common_ancestor():
	filename = raw_input("File: ")
	strands = []
	strand = ''
	counts = []
	final_string = ''
	a, t, g, c, = [], [], [], []
	with open(filename, "r") as openFile:
		for line in openFile:
			if re.match(r'>(\w*)', line):
				if strand:
					strands.append(strand.rstrip())
				strand = ''
			else:
				strand += line

	for i in range(0, len(strands[0]) - 1):
		a_0, t_0, g_0, c_0 = 0, 0, 0, 0

		for j in range(0, len(strands) - 1):
			if strands[j][i] == "A":
				a_0 += 1
			elif strands[j][i] == "T":
				t_0 += 1
			elif strands[j][i] == "G":
				g_0 += 1
			elif strands[j][i] == "C":
				c_0 += 1

		count = {'A': a_0, 'T': t_0, 'G': g_0, 'C': c_0}

		counts.append(count)

	for item in counts:
		max = ''
		max_val = 0
		for key in item:
			if key == 'A':
				max_val = item[key]
				max = 'A'
				a.append(item[key])
			else:
				if item[key] > max_val:
					max_val = item[key]
					max = key
				if key == 'T':
					t.append(item[key])
				elif key == 'G':
					g.append(item[key])
				elif key == 'C':
					c.append(item[key])
		final_string += max
	
	print final_string
	print "A: %s" % ' '.join(map(str, a))
	print "C: %s" % ' '.join(map(str, c))
	print "G: %s" % ' '.join(map(str, g))
	print "T: %s" % ' '.join(map(str, t))
	
common_ancestor()
