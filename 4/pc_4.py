import urllib,re

def get_nothing(nothing):
	url_base = r'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='
	try:
		for i in range(401):
			url = '%s%s' % (url_base, nothing)
			content = urllib.urlopen(url).read()
			tmp_nth = re.findall(r'\d+', content)
			nothing = tmp_nth[0]
			print content
	except Exception, e:
		print content
		tmp_nth = raw_input('Tell me the next nothing:')
		get_nothing(tmp_nth)
	

def main():
	get_nothing(63579)

if __name__ == '__main__':
	main()