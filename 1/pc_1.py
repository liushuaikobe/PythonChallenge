import sys,string

def parseStr(str):
	result = ''
	for c in str:
		if c in string.lowercase:
			tmp_str = ''
			if c == 'y':
				tmp_str = 'a'
			elif c == 'z':
				tmp_str = 'b'
			else:
				tmp_str = chr(ord(c) + 2)
			result = '%s%s' % (result, tmp_str)
			
		else:
			result = '%s%s' % (result, c)
	return result
def main():
	print parseStr(sys.argv[1])

if __name__ == '__main__':
	main()
