import re

def part1():
    # Parse through input file
    with open('days\day1\input.txt') as f:
        lines = f.read().splitlines()

    # Get values and sum up
    sum = 0
    for input in lines:
        # to lower
        input = input.lower()

        # remove letters with regex
        input = re.sub("[a-z]", "", input)

        # if there are more than 2 numbers, just take the first and last, and if there is only one number, then duplicate it
        if len(input) >= 2:
            input = input[0] + input[len(input) - 1]
        else:
            input = input[0] + input[0]

        # sum up numbers
        sum += int(input)

    # print sum
    print(sum)

mapping = {
    "one": "o1e",
    "two": "t2o",
    "three": "t3e",
    "four": "f4r",
    "five": "f5e",
    "six": "s6x",
    "seven": "s7n",
    "eight": "e8t",
    "nine": "n9e"
}

def part2():
    # Parse through input file
    with open('days\day1\input.txt') as f:
        lines = f.read().splitlines()
    
    # Get values and sum up
    sum = 0
    for input in lines:
        # to lower
        input = input.lower()

        # replace values in input using dictionary
        for key in mapping.keys():
            input = input.replace(key, mapping[key])

        # remove letters with regex
        input = re.sub("[a-z]", "", input)

        # if there are more than 2 numbers, just take the first and last, and if there is only one number, then duplicate it
        if len(input) >= 2:
            input = input[0] + input[len(input) - 1]
        else:
            input = input[0] + input[0]

        # sum up numbers
        sum += int(input)
    print(sum)

part2()