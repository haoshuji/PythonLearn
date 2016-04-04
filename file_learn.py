if __name__ == '__main__':
	xfile = open('romeo.txt')
	
	# count = 0
	# for line in xfile:
	# 	count = count + 1
	# print 'Line Count:',count

	# inp = xfile.read()
	# print len(inp)

	for line in xfile:
		line = line.rstrip()
		if not line.startswith('Python'):
			continue
		print line
	