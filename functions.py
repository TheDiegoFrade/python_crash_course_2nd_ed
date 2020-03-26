def describe_pet(animal_type, pet_name, attitude = 'ladilla'):
       """Display information about a pet."""
       print(f"\nI have a {animal_type}.")
       print(f"My {animal_type}'s name is {pet_name.title()}.")
       print(f"And is a {attitude}.")

describe_pet(animal_type ='dog', pet_name ='Odin el perro')


def get_formatted_name(first_name, last_name, middle_name=''):
       """Return a full name, neatly formatted."""
       if middle_name:
       		full_name = f"{first_name} {middle_name} {last_name}"
       else:
       		full_name = f"{first_name} {last_name}"
       return full_name.title()

pet = get_formatted_name('Odin', 'Perro')
print(pet)

pet = get_formatted_name('Odin', 'Perro', 'El')
print(pet)

def build_pet(first_name, last_name, age=None):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    if age:
    	person['age'] = age
    return person
pet = build_pet('Odin', 'Perro', 2)
print(pet)

while True:
    print("\nPlease tell me your pet's name:")
    print("(enter 'q' at any time to quit)")

    f_name = input("First name: ")
    if f_name == 'q':
        break

    l_name = input("Last name: ")
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}!")


#Copy of the list
#function_name(list_name[:])

#Unlimited number of arguments
def make_pizza(*toppings):
    """Print the list of toppings that have been requested."""
    print(toppings)

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

#Positional and unlimited arguments
def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')


#Arbitrary Keyword arguments
def build_profile(first, last, **user_info):
       """Build a dictionary containing everything we know about a user."""
       user_info['first_name'] = first
       user_info['last_name'] = last
       return user_info
user_profile = build_profile('albert', 'einstein',
                                location='princeton',
                                field='physics')
print(user_profile)