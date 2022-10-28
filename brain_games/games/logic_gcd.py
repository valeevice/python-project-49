from random import randint
import math


def question_unswer():
    random_number1 = randint(1, 100)
    random_number2 = randint(1, 100)
    print(f'Question: {random_number1} {random_number2}')
    correct_unswer = math.gcd(random_number1, random_number2)
    return str(correct_unswer)
