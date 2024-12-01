with open('books/frankenstein.txt') as f:
    file_contents = f.read()

print('--- Begin report of books/frankenstein.txt ---')

words = file_contents.split()
word_count = len(words)

print(f"{word_count} words found in the document")

letter_count = {}

for word in words:
    letters = list(word)

    # remove special characters
    letters = [letter.lower() for letter in letters if letter.isalpha()]

    for letter in letters:
        if letter_count.get(letter):
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1

for key, value in letter_count.items():
    print(f"The '{key}' character was found {value} times")

print('--- End report ---')