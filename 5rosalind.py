import re

def max_gc_content():
	filename = raw_input("Please enter the file path: ")
	max_id = ''
	max_count = 0.0
	id = ''
	str = ''
	with open(filename, "r") as openfile:
		for line in openfile:
			if re.match(r'>*\w', line):
				""" If the previous id had bigger gc_count, set max """
				if str and gc_count(str) > max_count:
					max_id = id
					max_count = gc_count(str)
						
				matchObj = re.match(r'\w', line)
				id = matchObj.group()
				str = ''
			else:
				str += line		
	print id, max_count
	

def gc_content(str):
        dna = str
        g_or_c = 0
        for i in dna:
                if i == "G" or i == "C":
                        g_or_c += 1

        print g_or_c / len(str)
        return g_or_c / len(str)

max_gc_content()
