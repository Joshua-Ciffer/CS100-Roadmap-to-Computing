"""
Joshua Ciffer
Homework 6 CS 100 029
September 23rd, 2019
"""

def hasFinalLetter(strList, letters):
    lst = []
    for str in strList:
        if str.endswith(letters):
            lst.append(str)
    return lst

def isDivisible(maxInt, twoInts):
    lst = []
    for x in range(maxInt):
        if x == 0:
            continue
        if (x % twoInts[0] == 0) and (x % twoInts[1] == 0):
            lst.append(x)
    return lst

def main():
    # 1
    list1 = ['Hello', 'Hi', 'Hey']
    let1 = 'lo'
    print('1: ' + str(hasFinalLetter(list1, let1)))
    list2 = ['Hello', 'No', 'Go?']
    let2 = 'o'
    print('2: ' + str(hasFinalLetter(list2, let2)))
    list3 = ['Yes', 'No', 'Maybe']
    let3 = 'a'
    print('3: ' + str(hasFinalLetter(list3, let3)))

    # 2
    int1 = 10
    ints1 = (2, 5)
    print('1: ' + str(isDivisible(int1, ints1)))
    int2 = 1
    ints2 = (3, 4)
    print('2: ' + str(isDivisible(int2, ints2)))
    int3 = 20
    ints3 = (2, 4)
    print('3: ' + str(isDivisible(int3, ints3)))

main()