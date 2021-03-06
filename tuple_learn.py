def tuple_test():
	fhand = open('romeo.txt')
	counts = dict()
	for line in fhand:
		words = line.split()
		for word in words:
			counts[word] = counts.get(word,0) + 1

	lst = list()
	for key, val in counts.items():
		lst.append((val,key))
		
	lst.sort(reverse=True)

	for val, key in lst[:10]:
		print key, val
if __name__ == '__main__':
	
	# read file, and output the top 10 most often words
	# tuple_test()

	# sort version of sort a dictionary by value
	c = {'a':10, 'b':1, 'c':22}
	print sorted( [ (v,k) for k,v in c.items() ], reverse=True)

	