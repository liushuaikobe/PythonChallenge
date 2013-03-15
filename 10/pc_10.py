def main():
	seq = '1'
	current_num = ''
	counter = 0
	a = seq[0]
	for i in xrange(5):
		for c in seq:
			if c == a:
				counter += 1
			else:
				current_num = ''.join((current_num, str(counter),a))
				counter = 1
		current_num = ''.join((current_num, str(counter),a))
		counter = 1
		print current_num
		seq = current_num
		current_num = ''

if __name__ == '__main__':
	main()