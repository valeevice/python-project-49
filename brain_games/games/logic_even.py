from brain_games import f_m
from random import randint

def question_unswer():
    random_number = randint(1, 1000)
    print(f'Question: {random_number}')
    correct_unswer = random_number % 2 == 0 and 'yes' or 'no'
    return correct_unswer


if __name__ == '__main__':
    main()
