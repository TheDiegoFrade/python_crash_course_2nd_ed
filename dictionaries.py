bicycles = {'trek':'green', 'cannondale':'blue', 'redline':'red', 'specialized':'gold'}
print(bicycles)
print(type(bicycles))
print(f'\nWe have a {bicycles["trek"]} Trek bicycle')

bicycles = {}
bicycles['trek'] = 'green'
bicycles['cannondale'] = 'blue'
bicycles['redline'] = 'red'
print(bicycles)

del bicycles['cannondale']
print(bicycles)

bicycle_value = bicycles.get('specialized',"Couldn't find bicycle with that name")
print(bicycle_value)

for key, value in bicycles.items():
	print(f'\nKey: {key} Value: {value}')

for bike in bicycles.keys():
	print(f'\nBike: {bike}')

for color in bicycles.values():
	print(f'\nBike Color: {color}')

#You can create a list of dictionaries

#Or a list inside a dictionary
pizza = {
       'crust': 'thick',
       'toppings': ['mushrooms', 'extra cheese'],
       }
print(f'You ordered a {pizza["toppings"][0]} & {pizza["toppings"][1]} pizza.')

#You can also nest a dictionary inside a dictionary but your code may get complicated.

