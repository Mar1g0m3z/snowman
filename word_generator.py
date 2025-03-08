from wonderwords import RandomWord
# import game
from game import SNOWMAN_MAX_WORD_LENGTH
# from game import SNOWMAN_MAX_WRONG_GUESSES
from game import SNOWMAN_MIN_WORD_LENGTH


def generate_random_word():

    random_word_generator = RandomWord()
    return random_word_generator.word(
        word_min_length=SNOWMAN_MIN_WORD_LENGTH,
        word_max_length=SNOWMAN_MAX_WORD_LENGTH
    )
