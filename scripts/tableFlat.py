# coding=utf-8
import csv



with open('/Users/jancibulka/DEVEL/IHNED/volici-2013-praha-zastavba/data/oblastiKatastr.csv', 'r') as csvfile:
	reader = csv.reader(csvfile, delimiter=',', quotechar='"')
	print 'NAZKU' + '	' + 'OBJID'
	for row in reader:
		if (row[0] == 'OBJECTID'):
			continue
		katastry = row[2].split('území: ')[1].strip(')').split(', ')
		for katastr in katastry:
			print katastr + '	' + row[0]