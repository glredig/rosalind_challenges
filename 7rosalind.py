def rev_palindrome():
	f = raw_input("File: ")
	dna = ''
	with open(f, "r") as openFile:
		id = openFile.readline()
		for line in openFile:
			dna += line.rstrip()
		
	for i in range(1, len(dna)):
		#print i
		if i + 1 < len(dna) and are_complements(dna[i], dna[i + 1]):
			check_palindrome(i, i + 1, dna)
				  



def are_complements(a, b):
	if a == 'A':
		return b == 'T'
	elif a == 'T':
		return b == 'A'
	elif a == 'G':
		return b == 'C'
	elif a == 'C':
		return b == 'G'

def check_palindrome(i, j, dna):
	#print dna
	distance = 1
	total_length = 2
	while (distance <= 6 and (i - distance >= 0) and (j + distance <= len(dna) - 1)):
		#print "while", dna[i - distance], dna[j + distance]
		if are_complements(dna[i - distance], dna[j + distance]):
			total_length += 2
			print i - distance + 1, total_length
			distance += 1
		else:
			break		
	if total_length >= 4:
		return i - distance + 2, total_length
	else:
		return False

rev_palindrome()
