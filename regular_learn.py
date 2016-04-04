import re
if __name__ == '__main__':
	hand = open('romeo.txt')
	for line in hand:
		line = line.strip()
		if re.search('^The', line):
			print line

	x = 'My 2 favorite numbers are 19 and 42'
	y = re.findall('[0-9]+',x)
	print y

	# greedy math, longest
	x = 'From: Using the :character'
	y = re.findall('^F.+:',x)
	print y

	#non-greedy one, shortest one
	y = re.findall('^F.+?:',x)
	print y

	x = 'From stephen.marquare@uct.ac.za Sat Jan 2009'
	y = re.findall('\S+@\S+',x)
	print y

	y = re.findall('^From (\S+@\S+)',x)
	print y

	y = re.findall('@([^ ]+)', x)
	print y

	y = re.findall('^From .*@([^ ]*)',x)
	print y