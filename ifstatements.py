bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(f'\nIf statement:')
for bike in bicycles:
	if bike == 'trek':
		print(f'\t{bike.upper()}')
	elif bike == 'redline':
		print(f'\t{bike.lower()}')
	else: 
		print(f'\t{bike.title()}')
print(f'\nOther way around:\n')
for bike in bicycles:
	if bike != 'trek':
		print(f'\t{bike.upper()}')
	elif bike == 'specialized':
		print(f'\t{bike.lower()}')
	else: 
		print(f'\t{bike.title()}')

print(f'Are there more than 2 bicycles? {len(bicycles)>2}\n')
print(f'Is there a specialized bike? {"specialized" in bicycles}')

#You can use as many elif as you want and else is not requiered. 