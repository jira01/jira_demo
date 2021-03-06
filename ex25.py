from traceback import print_tb


def break_words(stuff):
    words = stuff.split(' ')
    return words

def sort_words(words):
    return sorted(words)

def print_first_word(words):
    word = words.pop(0)
    print(word)

def print_last_word(words):
    word = words.pop(-1)
    print(word)

def sort_sentence(sentence):
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    words = break_words(sentence)
    print(words)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)

def test():
    print('test')


def test_02():
    print('test_02')

def test_03():
    print('test_03')


def test_04():
    print('test_04')

def test_05():
    print('test_05')


def test_07():
    print('test_07')

def test_06():
    print('test_06')

