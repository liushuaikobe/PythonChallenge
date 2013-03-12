import bz2

# It must be admitted that I found bzip2 via Google 
# It said that 'BZh91AY' is a typical header of a bzip2 sequence
# wikipedia(in Chinese):http://zh.wikipedia.org/wiki/Bzip2

def main():
	un = 'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
	pw = 'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08'

	print bz2.decompress(un)
	print bz2.decompress(pw)

if __name__ == '__main__':
	main()
