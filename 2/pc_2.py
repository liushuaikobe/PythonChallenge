import sys,urllib,re,operator

def readMess(url):
	html = urllib.urlopen(url).read()
	result = re.findall(r'<!--[\s\S]*?-->', html)
#	print result[1][5:len(result[1])-3]
	return result[1][5:len(result[1]) - 3]

def statistics(mess):
	char_dic = {}
	order = []
#	If you have copied the mess in a local txt file,open it.
#	mess = open(sys.argv[1], 'r')
#	for eachLine in mess.readlines():
#		for c in eachLine.strip():
#			if c in char_dic:
#				char_dic[c] += 1
#			else:
#				char_dic[c] = 1
#	print char_dic
	for c in mess:
		if c != '\n':
			if c in char_dic:
				char_dic[c] += 1
			else:
				char_dic[c] = 1
				order.append(c)
	print 'Result:'
	print sorted(char_dic.iteritems(), key = operator.itemgetter(1), reverse = True)
	print 'Order:'
	print order

def main():
	url = 'http://www.pythonchallenge.com/pc/def/ocr.html'
	statistics(readMess(url))
	readMess(url)

if __name__ == '__main__':
	main()
