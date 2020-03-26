class Dog:
	"""Attempt to model a dog."""
	#__init__ is a special method that runs when we create a new instance bases on a class
	#self parameter is required
	def __init__(self,name,age):
		"""Initialize name and age attributes"""
		self.name = name
		self.age = age
		self.money = 0

	#A function that is part of a class is a method	
	def sit(self):
		"""Simulate a dog sitting in response to a command"""
		print(f'{self.name} is now sitting.')

	def roll_over(self):
		"""Simulate a dog rolling over in response to a command"""
		print(f'{self.name} is rolling over.')

	def money_odometer(self):
           """Print a statement showing the car's mileage."""
           print(f"This dog has {self.money}$ in his wallet.")
	
	def update_odometer(self, new_money):
       		"""Set the odometer reading to the given value."""
       		if new_money >= self.money:
       			self.money = new_money
       		else:
       			print("This dog has less money now.")

	def increment_odometer(self,new_money):
		self.money += new_money

#Inheritance
class Robotdog(Dog):
	"""Represent aspects of a car, specific to electric vehicles."""

	def __init__(self, name, age):
    		"""Initialize attributes of the parent class."""
    		super().__init__(name, age)
    		self.battery_size = 75

	def describe_battery(self):
			"""Print a statement describing the battery size."""
			print(f"This Robot Dog has a {self.battery_size}-kWh battery.")

	#You can also override meaningless functions in the inheritance

	#Also if we would like to add more and more functions or descriptions to the battery the we would need
	#To create a battery class. 

	#Don’t be discouraged if you find you’re ripping apart your classes and rewriting them several times 
	#using different approaches. In the quest to write accurate, efficient code, 
	#everyone goes through this process.


    		

my_dog = Dog('Odin',2)
print(f"My dog's name is {my_dog.name}")
print(f"My dog is {my_dog.age} years old")

my_dog.sit()

my_dog.roll_over()

my_dog.money = 40

my_dog.update_odometer(50)

my_dog.money_odometer()

my_dog.increment_odometer(200)

print(f"{my_dog.name} now has {my_dog.money}$\n")


my_robot_dog = Robotdog('Robo-Odin',2)
print(f"My Robot dog's name is {my_robot_dog.name}")
print(f"My Robot dog is {my_robot_dog.age} years old")

my_robot_dog.sit()

my_robot_dog.roll_over()

my_robot_dog.money = 40

my_robot_dog.update_odometer(50)

my_robot_dog.money_odometer()

my_robot_dog.increment_odometer(200)

print(f"{my_robot_dog.name} now has {my_robot_dog.money}$")

my_robot_dog.describe_battery()










		