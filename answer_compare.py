def compare():
	my_filename = raw_input("Your file: ")
	other_filename = raw_input("Other file: ")
	
	their_answers = []
	my_answers = []
	missing = []
	extra = []

	print "Comparing answers...\n"
	
	with open(other_filename, 'r') as otherOpenFile:
		for line in otherOpenFile:
			their_answers.append(line)

	with open(my_filename, 'r') as myOpenFile:
		for line in myOpenFile:
			my_answers.append(line)

	print "Number of their answers: %s" % (len(their_answers))
	print "Number of your answers: %s" % (len(my_answers))
	print "-----------------------------------\n"

	for i in xrange(len(their_answers)):
		if their_answers[i] not in my_answers:
			missing.append(their_answers[i])

	for j in xrange(len(my_answers)):
		if my_answers[j] not in their_answers:
			extra.append(my_answers[j])

	print "==================================="
	print "Missing: "
	print missing
	print "==================================="
	print "Extra: "
	print extra

compare()
