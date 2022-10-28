from brain_games import f_m
from random import randint
import math

# https://foxford.ru/wiki/informatika/proverka-chisla-na-prostotu-v-python
def isPrime(n):
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n and n % d != 0:
        d += 2
    return d * d > n

def question_unswer():
    number = randint(1, 1500)
    print(f'Question: {number}')
    correct_unswer = isPrime(number) and 'yes' or 'no'
    return str(correct_unswer)