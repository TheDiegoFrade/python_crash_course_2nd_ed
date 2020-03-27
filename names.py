from name_function import get_formatted_name

print("Enter 'q' any time to quit")
while True:
	first = input(f"\nPlease give me first name: ")
	if first == 'q':
		break
	middle = input(f"\nPlease give me middle name: ")
	if middle == 'q':
		break
	last = input(f"\n Please give me last name: ")
	if last == 'q':
		break
	formatted_name = get_formatted_name(first,last,middle)
	print(f"\tNeatly formatted name: {formatted_name}")
