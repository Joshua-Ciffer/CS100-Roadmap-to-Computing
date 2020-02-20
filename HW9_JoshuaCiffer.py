'''
Joshua Ciffer
CS 100 029 HW9
November 13th, 2019
'''
	
def file_copy(in_file, out_file):
	input = open(in_file, 'r')
	output = open(out_file, 'w')
	for line in input:
		output.write(line)
	input.close()
	output.close()

def file_stats(in_file):
	text = open(in_file, 'r')
	num_lines = 0
	num_words = 0
	num_characters = 0
	lines = text.readlines()
	for line in lines:
		num_lines += 1
		for word in line.split():
			num_words += 1
			for char in word.split():
				num_characters += 1
	print('Lines: ' + str(num_lines) + '\nWords: ' + str(num_words) + '\nCharacters: ' + str(num_characters))