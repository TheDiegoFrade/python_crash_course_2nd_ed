bicycles = ['trek', 'cannondale', 'redline', 'specialized']
message = f"My first bicycle was a {bicycles[0].title()}\nMy last bicycle was a {bicycles[-1].title()}\n"
print(message)

bicycles[-1] = 'scott'
message = f"My first bicycle was a {bicycles[0].title()}\nMy last bicycle was a {bicycles[-1].title()}\n"
print(message)

#Insert into specific space in list
bicycles.insert(0,'benotto')
message = f"My first bicycle was a {bicycles[0].title()}\nMy last bicycle was a {bicycles[-1].title()}\n"
print(message)

#Insert into last space in list
bicycles.append('mercurio')
message = f"My first bicycle was a {bicycles[0].title()}\nMy last bicycle was a {bicycles[-1].title()}\n"
print(message)

#Append values into an empty list
bicycles_i_dont_like = []
bicycles_i_dont_like.append('mercurio')
bicycles_i_dont_like.append('benotto')
bicycles_i_dont_like.append('specialized')
print(bicycles_i_dont_like)

#I like specialized
del bicycles_i_dont_like[-1]
print(bicycles_i_dont_like)

#pop method
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
first_used = bicycles.pop(0)
last_used = bicycles.pop()
print(f'\nPop:')
print(f'\t1. {first_used.title()}')
print(f'\t2. {last_used.title()}')

print(f'\nList after pop:')
print(f'\t{bicycles}')

#Remove
bicycles.remove('redline')
print(f'\nList after remove:')
print(f'\t{bicycles}')

#Sort
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(f'\nList before sort:')
print(f'\t{bicycles}')
print(f'\nList after sort:')
bicycles.sort()
print(f'\t{bicycles}')
bicycles.reverse()
print(f'\nList after reverse sort:')
print(f'\t{bicycles}')

#Length
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(f'\nList length:')
print(f'\t{len(bicycles)}')

#Looping
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
index = list(range(0,4))

print(f'\nBikes in List:')
for number in index:
	print(f'{number + 1}. {bicycles[number].title()}')

#Create loop list in one line
index = [number+1 for number in range(0, 4)]
print(f'\nOne line list:')
print(f'{index}')

#Slicing a list
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(f'\nSlicing:')
print(bicycles[:1])
print(bicycles[:3])
print(bicycles[:])

#Copying List
bicycles_i_like = bicycles[:3]
print(f'\nCopy:')
print(bicycles_i_like)

#Tuple
#A tuple is an unmutable list
print(f'\nType:')
bicycles = ('trek', 'cannondale', 'redline', 'specialized')
print(type(bicycles))


