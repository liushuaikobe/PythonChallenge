import StringIO,urllib2,pickle

def serialize(mess):
	file = StringIO.StringIO()
	pickle.dump(mess, file, 0)
	return file.getvalue()

def de_serialize(mess):
	return pickle.loads(mess)

def draw(lst):
	for item in lst:
		s = ''
		for t in item:
			s += t[0] * t[1]
		print s

def main():
	mess = urllib2.urlopen(r'http://www.pythonchallenge.com/pc/def/banner.p').read()
#	print serialize(mess)
	result =  de_serialize(mess)
	draw(result)

if __name__ == '__main__':
	main()
