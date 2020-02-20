'''
Joshua Ciffer
CS 100 029 HW10
November 13th, 2019
'''

def main():
	horton = ['I', 'say', 'what', 'I', 'mean', 'and', 'I', 'mean', 'what', 'I', 'say']
	#print(initialLetterCount(horton))
	#print(initialLetters(horton))
	#print(shareALetter(horton))

def initialLetterCount(wordList):
	dic = {}
	for word in wordList:
		dic[word[0:1]] = 0
	for firstLetter in dic.keys():
		for word in wordList:
			if firstLetter == word[0:1]:
				dic[firstLetter] += 1
	return dic

def initialLetters(wordList):
	dic = {}
	for word in wordList:
		dic[word[0:1]] = []
	for firstLetter in dic.keys():
		for word in wordList:
			if firstLetter == word[0:1] and word not in dic[firstLetter]:
				dic[firstLetter].append(word)
	return dic

def shareALetter(wordList):
	dic = {}
	for word in wordList:
		dic[word] = []
	for keyword in dic.keys():
		for letter in keyword:
			for word in wordList:
				if letter in word and word not in dic[keyword]:
					dic[keyword].append(word)
	return dic

main()