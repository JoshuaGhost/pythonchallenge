import png

with open('oxygen.png') as pngfile:
	r = png.Reader(file=pngfile)
	l = list(r.read()[2])
	print l[0]
	for i in r.read()[2]:
		pass
