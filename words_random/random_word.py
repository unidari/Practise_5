import random

with open('word list.txt', encoding='utf-8') as file:
    words = file.read().split(' ')

def r_word():
    return random.choice(words)