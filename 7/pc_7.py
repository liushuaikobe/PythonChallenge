from PIL import Image 

img = Image.open(r'oxygen.png')
# print img.format
# print img.info
# print img.mode
a,b,c,d = img.split()
a.save('a.png')
b.save('b.png')
c.save('c.png')
d.save('d.png')