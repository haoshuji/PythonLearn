import socket
import urllib
from BeautifulSoup import *

def socket_test():
	mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	mysock.connect(('www.py4inf.com',80))
	mysock.send('GET http://www.py4info.com/code/romeo.txt HTTP/1.0\n\n')

	while True:
		data = mysock.recv(512)
		if (len(data)<1):
			break
		print data

	mysock.close()

def urllib_test():
	fhand = urllib.urlopen('http://www.py4inf.com/code/romeo.txt')	
	# print dir(fhand)
	for line in fhand:
		print line.strip()
	fhand.close()

	fhand = urllib.urlopen('http://www.dr-chuck.com/page1.htm')
	# print fhand.url # get the url of current fhand
	for line in fhand:
		print line.strip()

def soup_test():
	html = urllib.urlopen('http://www.dr-chuck.com/page1.htm').read()
	soup = BeautifulSoup(html)
	tags = soup('a')

	for tag in tags:
		print tag.get('href', None)

if __name__ == '__main__':
	# socket_test()
	urllib_test()
	soup_test()
