from PIL import Image 

def get_img(path):
	return Image.open(path)

def main():
	img = get_img('oxygen.png')
	# when we run this script first,it tell us the mode of this png is RGBA
	print img.mode
	y_begin = 0
	while True:
		pi = img.getpixel((0,y_begin))
		# The value R == G == B in Gray
		if pi[0] == pi[1] == pi[2]:
			break
		y_begin += 1
	x_end = 0
	while True:
		pi = img.getpixel((x_end,y_begin))
		if not pi[0] == pi[1] == pi[2]:
			break
		x_end += 1
	print x_end
	gray = []
	# I first try to get ans by recording the no-repeat R(or G or B) value of gray bar,however,it is infeasible,like the '11' in '115'.
	# The number of step 7 is from where I saw a blog called UnixWars.
	for i in range(0,x_end,7):
		gray.append(img.getpixel((i,y_begin))[0])
	print gray
	print ''.join([chr(c) for c in gray])
	# After running the scipt above,we get the next level:[105, 110, 116, 101, 103, 114, 105, 116, 121]
	print ''.join([chr(c) for c in [105, 110, 116, 101, 103, 114, 105, 116, 121]])

if __name__ == '__main__':
	main()