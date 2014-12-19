import itertools

def func(length):
	table = {
		('1','1','1'):'31',
		('1','1','1'):'21',
		('1',):'11',
		('2','2','2'):'32',
		('2','2'):'22',
		('2',):'12',
		('3','3','3'):33,
		('3','3'):23,
		('3'):'13'
	}
	s, answer = '1',[1]
	a=itertools.groupby(s)
	print(a,b)
	for i in range(length-1):
		c = "".join(table[tuple(l)] for e, l in itertools.groupby(prec))
		s = ''.join(table[tuple(l)] for e, l in itertools.groupby(s))
		answer.append(int(s))
		print(s)

	return answer

print(len(str(func(31)[30])))

