import re

def max_gc_content():
	filename = raw_input("Please enter the file path: ")
	max_id = ''
	max_count = 0.0
	id = ''
	str = ''
	with open(filename, "r") as openfile:
		for line in openfile:
			if re.match(r'>(\w){13}', line):
				""" If the previous id had bigger gc_count, set max """
				if str:
					if gc_count(str) > max_count:
						max_id = id
						max_count = gc_count(str)
						
				matchObj = re.match(r'>(\w){13}', line)
				id = matchObj.group(0)
				str = ''
			else:
				matchObj = re.match(r'[^\s]*', line)
				str += matchObj.group(0)

		if gc_count(str) > max_count:
			max_id = id
			max_count = gc_count(str)		
	print max_id[1:]
	print  max_count * 100.0
	

def gc_count(str):
        dna = str
        g_or_c = 0.0
        for i in dna:
                if i == "G" or i == "C":
                        g_or_c += 1
	#print g_or_c / float(len(dna))
	return g_or_c / float(len(dna))

max_gc_content()
