def main():
	# Look-and-say sequence
	# http://en.wikipedia.org/wiki/Look-and-say_sequence
	seq = '1'
	current_num = ''
	counter = 0
	a = seq[0]
	# print seq
	for i in xrange(30):
		for c in seq:
			if c == a:
				counter += 1
			else:
				current_num = ''.join((current_num, str(counter),a))
				a = c
				counter = 1
		current_num = ''.join((current_num, str(counter),a))
		# print current_num
		seq = current_num
		counter = 0
		current_num = ''
		a = seq[0]
	print len(seq)

if __name__ == '__main__':
	main()