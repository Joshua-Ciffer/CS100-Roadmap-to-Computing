"""
Joshua Ciffer
CS 100 029 HW11
November 13th, 2019
"""

class Dog:
	'''Object representation of a dog.'''
	
	species = 'canis familiaris'
	
	def __init__(self, name, breed):
		'''Initializes a dog object.'''
		self.name = name
		self.breed = breed
		self.tricks = []
	
	def teach(trick):
		'''Teaches a trick to the dog.'''
		self.tricks.append(trick)
		print(name + ' knows ' + trick + '.')
	
	def knows(trick):
		'''Checks to see if the dog knows a certain trick.'''
		if trick in self.tricks:
			print(name + ' does know ' + trick + '.')
			return True
		else:
			print(name + ' does not know ' + trick + '.')
			return False