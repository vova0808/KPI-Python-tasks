def create_calendar_page(m=4, y=2015):
	import calendar
	s=''
	lin='--------------------\nMO TU WE TH FR SA SU\n--------------------\n'
	c = calendar.Calendar()
	for i in c.monthdayscalendar(y, m):
		for q in i:
			q=str(q)
			if q=='0': q=q.replace('0', '  ')
			if len(q)==1: q='0'+q
			s=s+q+' '
		s=s+'\n'
	s=s.replace(' \n', '\n')
	return lin+s

print create_calendar_page(1, 2020)
