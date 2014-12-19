import Image 

answer = ''
with Image.open('oxygen.png') as pngfile:
	print pngfile.size
	for x in range(0,pngfile.size[0],7):
		pix = pngfile.getpixel((x,50))
		if pix[0] == pix[1] and pix[1] == pix[2]:
			answer+=chr(pix[0])
print answer
t = [105, 110, 116, 101, 103, 114, 105, 116, 121]
answer = ''
for l in t:
	s = ''
	for i in str(l):
		s += i
	answer+=chr(int(s))
print answer
