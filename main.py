import unittest
from word_generator import generate_random_word
if __name__ == '__main__':
    # Get a random word 5-8 letters long
    user_input = ""
    while user_input != "p" and user_input != "t":
        user_input = input('Please enter p to play or t to test => ')

    if user_input == "p":
        from game import snowman, SNOWMAN_MIN_WORD_LENGTH, SNOWMAN_MAX_WORD_LENGTH
        from wonderwords import RandomWord

        snowman_word = generate_random_word()
        snowman(snowman_word)
    else:
        from game_test import *
        unittest.main(exit=False)
