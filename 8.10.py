# Name: - Neeraj Kumar
# ID: - 2047559
word = str(input())
spaceless_word = word.replace(" ", "")
new = spaceless_word[::-1]

if spaceless_word == new:
    print('{} is a palindrome'.format(word))
else:
    print('{} is not a palindrome'.format(word))