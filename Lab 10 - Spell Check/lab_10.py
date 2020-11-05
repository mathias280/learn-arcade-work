import re


def split_line(line):
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?', line)


def linear_search(key, list):

    current_position = 0
    while current_position < len(list) and list[current_position] != key:
        current_position += 1
    if current_position == len(list):
        return False
    else:
        return True


def binary_search(key, list):

    lower_bound = 0
    upper_bound = len(list) - 1
    found = False
    while lower_bound <= upper_bound and not found:
        middle_pos = (lower_bound + upper_bound) // 2
    if list[middle_pos] == key:
        found = True
    elif list[middle_pos] < key:
        lower_bound = middle_pos + 1
    elif list[middle_pos] > key:
        upper_bound = middle_pos - 1
    return found


# Dictionary
dictionary_list = open("dictionary.txt")
correct_list = []

for line in dictionary_list:
    line = line.strip()
    correct_list.append(line)

dictionary_list.close()


# Alice In WonderLand200 (Linear)
print("\n-------LINEAR SEARCH-------")
story = open("AliceInWonderLand200.txt")
line_position = 1

for line in story:
    word_list = split_line(line)

    for word in word_list:
        word = word.upper()
    if not linear_search(word, correct_list):
        print("Possible misspelled word:", word, "at line", line_position)
        line_position += 1
story.close()

# Alice In WonderLand200 (Binary)
print("\n-------BINARY SEARCH-------")
story = open("AliceInWonderLand200.txt")
line_position = 1
for line in story:
    word_list = split_line(line)
    for word in word_list:
        word = word.upper()
    if not binary_search(word, correct_list):
        print("Possible misspelled word:", word, "at line", line_position)
        line_position += 1

story.close()


def main(key, list):
    print(linear_search(key, list))
    print(binary_search(key, list))


main()
