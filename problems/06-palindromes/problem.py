# Find all of the palindromes with at least 5 letters in the word list
# words.txt. Print each one, and also write them to a new file called
# palindromes.txt, one word per line.
#
# A palindrome is a word that reads the same forwards and backwards.
#
# The output should be:
#
# level
# stats
# refer
# radar
# civic
# xanax
#
# Hint: you can reverse a string with word[::-1]
#
# Hint: open the output file with open("palindromes.txt", "w"), and use
# .write() to add text to it. Remember that .write() doesn't add a newline
# for you, so you'll need to add "\n" to the end of each word.

with open("words.txt") as file:
    words = file.read().split()

# Your code goes here
