import string,sys

def parseStr(str):
	_from = string.lowercase
	_to = '%s%s' % (_from[2:], _from[0:2])
	table = string.maketrans(_from, _to)
	return str.translate(table)

def main():
	print parseStr(sys.argv[1])

if __name__ == '__main__':
	main()
