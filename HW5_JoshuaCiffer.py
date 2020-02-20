"""
Joshua Ciffer
HW5 CS 100 Section 029
September 17th, 2019
"""

# 1
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
for month in months:
	if month[0].lower() == 'j':
		print(month)

# 2
for x in range(99):
	if (x % 2 == 0) and (x % 5 == 0):
		print(x)

# 3
horton = "A person's a person, no matter how small."
vowels = "aeiouAEIOU"
for x in horton:
	if x in vowels:
		print(x)
