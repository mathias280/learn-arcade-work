import re


def split_line(line):
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?', line)


def main():

    dictionary_list = open("dictionary.txt")

    name_list = []

    for line in dictionary_list:
        line = line.strip()
        name_list.append(line)

    dictionary_list.close()

# Linear search

    story = open("AliceInWonderLand200.txt")

    for line in story:
        split_line(story)
        word_list = split_line(story)
        for word in word_list:

    key = "story"

    story.close()


main()