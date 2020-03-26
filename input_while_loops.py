#number = input("Enter a number, and I'll tell you if it's even or odd: ")
#number = int(number)

#if number % 2 == 0:
#    print(f"\nThe number {number} is even.")
#else:
#    print(f"\nThe number {number} is odd.")

current_number = 1
while current_number <= 5:
	print(current_number)
	current_number += 1

#prompt = "\nTell me something, and I will repeat it back to you:"
#prompt += "\nEnter 'quit' to end the program. "

#message = ""
#while message != 'quit':
#    message = input(prompt)

#    if message != 'quit':
#        print(message)

# prompt = "\nPlease enter the name of a city you have visited:"
#    prompt += "\n(Enter 'quit' when you are finished.) "

#Using break
# ➊ while True:
#        city = input(prompt)

#        if city == 'quit':
#            break
#        else:
#            print(f"I'd love to go to {city.title()}!")

unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

   # Verify each user until there are no more unconfirmed users.
   #  Move each verified user into the list of confirmed users.
while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)

# Display all confirmed users.
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
	print(confirmed_user.title())

pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(f'\n{pets}')

while 'cat' in pets:
    pets.remove('cat')

print(pets)
