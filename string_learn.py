def test():
	pass
if __name__ == '__main__':
	test()
	str1 = 'Hello'
	str2 = 'there'
	bob = str1 + str2
	print bob
	
	# name = raw_input('Enter:')
	# print name

	fruit = 'banana'
	# for letter in fruit:
	# 	print letter

	word = 'banana'
	count = 0
	for letter in word:
		if letter == 'a':
			count = count + 1
	print count

	greet = 'Hello Bob'
	zap = greet.lower()
	print greet, zap
	print greet.upper()	
	print 'Hi There'.lower()

	print fruit.find('na')
	print fruit.find('z')

	nstr = greet.replace('Bob', 'Jane')
	print nstr

	print greet.replace('o', 'X')

	greet = ' Hello Bob'
	print greet
	print greet.lstrip()
	print greet.rstrip()
	print greet.strip()

	line = 'Please have a nice day!'
	print line.startswith('Please')
	print line.startswith('z')

	#find the host
	data = 'From stephen.marquard@uct.zc.za Sat Jan 5 09:14:16 2008'
	print data
	atpos = data.find('@')	
	print atpos
	sppos = data.find(' ',atpos)
	print sppos
	host = data[atpos+1:sppos]
	print host

	