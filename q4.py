def is_leap_year(a_year):
	print(f'\n{str(a_year)} is a leap year.')
	if a_year%4 == 0:
		print('True')
	else: 
		print('False')
a_year = 2020
is_leap_year(a_year)