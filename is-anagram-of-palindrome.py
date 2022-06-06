# Challenge: https://fellowship.hackbrightacademy.com/materials/challenges/anagram-of-palindrome/index.html#anagram-of-palindrome

def is_anagram_of_palindrome(word):
    """Is the word an anagram of a palindrome?"""

    # store count of letter
    letter_count = {}

    # add letter count to dictionary
    for letter in word:
        letter_count[letter] = letter_count.get(letter, 0) + 1
    
    # there can only a max of 1 instance where letter count is odd
    # if odd_check falls below 0, there are too odd letter counts
    odd_check = 1

    for key in letter_count.keys():
        if letter_count[key] % 2 == 1:
            odd_check = odd_check - 1
            if odd_check == -1:
                return False
    
    return True