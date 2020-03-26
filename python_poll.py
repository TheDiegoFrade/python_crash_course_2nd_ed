responses = {}

# Set a flag to indicate that polling is active.
polling_active = True

while polling_active:
       # Prompt for the person's name and response.
	name = input("\nWhat is your name? ")
	response = input("Which are your favorite tacos? ")

       # Store the response in the dictionary.
	responses['name'] = name
	responses['flavor'] = response
       # Find out if anyone else is going to take the poll.
	repeat = input("Would you like to tell me something else about you?(yes/no)")
	if repeat.lower() == 'no':
		polling_active = False
		comment = ""
		print(comment)
		print("Goodbye!")
	else: 
		comment = input("Write your comment please: ")
		polling_active = False
		print(comment)
		print("Goodbye!")
	responses['comment'] = comment
	print(responses.items())
   # Polling is complete. Show the results.
print("\n--- Poll Results ---")
for value in responses.values():
	print(value)

print(f'Poll Dictionary: {responses}')

print("\n--- Poll Results ---")
for item in responses.items():
	print(item)