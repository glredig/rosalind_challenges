def gc_content():
	filename = raw_input("Please enter the file path: ")
	file = open(filename, "r")
	print file.readline()
	print file.readline()
	file.close()


gc_content()
