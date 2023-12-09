import re

with open("input.txt", "r") as input_stream:
    data = input_stream.read()

# data = '''two1nine
# eightwothree
# abcone2threexyz
# xtwone3four
# 4nineeightseven2
# zoneight234
# 7pqrstsixteen
# onetwoone'''

translation_dict = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
    }

def find_first_digit(word):
    temp = ""
    for char in word:
        temp += char
        for each in translation_dict:
            temp = temp.replace(each, translation_dict[each])
    if temp[0].isdigit():
        return temp[0]
    else:
        temp = re.sub("[^0-9\n]", "", temp)
        return temp[0]

def find_last_digit(word):
    word = word[::-1]  # reverse the string
    temp = ""
    for char in word:
        temp = char + temp
        for each in translation_dict:
            temp = temp.replace(each, translation_dict[each])
    if temp[-1].isdigit():
        return temp[-1]
    else:
        temp = re.sub("[^0-9\n]", "", temp)
        return temp[-1]
    

new_data = []
for word in data.split("\n"):
    print(f"raw word is {word}")
    first_digit = find_first_digit(word)
    print(f"first digit is {first_digit}")
    last_digit = find_last_digit(word)
    print(f"last digit is {last_digit}")
    new_data.append(int(f"{first_digit}{last_digit}"))

print(new_data)

totals = sum(new_data)
print(totals)