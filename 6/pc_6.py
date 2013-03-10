import zipfile,re,sys

def find_ans(mzipfile,start_no):
	file_list = [start_no]
	current_no = start_no
	try :
		for i in xrange(1000):
			content = mzipfile.read(current_no + '.txt')
			current_no = re.findall(r'\d+', content)[0]
			file_list.append(current_no)
			print current_no
	except Exception,e:
		print content
	finally:
		return file_list

def collect_comments(mzipfile, file_list):
	return ''.join([mzipfile.getinfo(i + '.txt').comment for i in file_list])

def main():	
	mzipfile = zipfile.ZipFile(sys.argv[1], 'r')
	file_list = find_ans(mzipfile,sys.argv[2])
	print collect_comments(mzipfile, file_list)

if __name__ == '__main__':
	main()