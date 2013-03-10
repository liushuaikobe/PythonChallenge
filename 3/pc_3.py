import sys, re, string

char = []
index = 0

def find_letters(path):
	mess = ''
	letters = open(path,'r')
	for eachLine in letters:
		mess = '%s%s' % (mess, eachLine.strip())
	handleMess('AAApAAAw' + mess + 'wEEEpTTT')
#	Can regex be feasible?Think twice.
#	Maybe the Author is kindness,it is feasible.
#	But,After Reading the riddle twice,you must understand the meaning of 'exactly'.Good luck!
# 	print re.findall(r'[a-z][A-Z]{3}[a-z][A-Z]{3}[a-z]',mess)

def handleMess(mess):
	global char, index
	while index < len(mess) - 8:
		flag = True
		for i in range(9):
			if i != 0 and i != 4 and i != 8:
				if mess[index + i] in string.uppercase:
					pass
				else:
					index += get_displacement(i)
					flag = False
					break
			else:
				if mess[index + i] in string.lowercase:
					if i == 4:
						c = mess[index + i]
				else:
					index += get_displacement(i)
					flag = False
					break
		if flag:
			char.append(c)
			index += 4
	prefix = mess[:8]
	tmp = re.findall(r'[A-Z]{3}[a-z][A-Z]{3}[a-z]',prefix)
	if len(tmp) != 0:
		char.insert(0,tmp[0][3])
	hostfix = mess[len(mess)-8:]
	tmp = re.findall(r'[a-z][A-Z]{3}[a-z][A-Z]{3}',hostfix)
	if len(tmp) != 0:
		char.append(tmp[0][4])

def get_displacement(i):
	if i == 0 or i == 4 or i == 8:
		return i + 1
	else:
		return i

def main():
	global char
	path = sys.argv[1]
	find_letters(path)
	print len(char)
	print char

if __name__ == '__main__':
	main()
