import urllib.request
from zipfile import *
import re

answer = ''

with ZipFile('channel.zip', 'r') as z:
	'''z = zipfile.ZipFile('channel.zip')'''
	fileName = '90052'
	while True:
		bline = z.read(fileName+'.txt')
		answer+=bytes.decode(z.getinfo(fileName+'.txt').comment)
		fileName = ''
		line = bytes.decode(bline)
		for c in line:
			if c.isdigit():
				fileName+=c
		if fileName == '':
			break
	print(answer)

