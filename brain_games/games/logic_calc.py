from brain_games import f_m
from random import choice
from random import randint
import operator

get_operator = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
}.get 

def calculate(x, y, operator):
    op = get_operator(operator)
    return (str(op(x, y)))

def question_unswer():
    random_number1 = randint(1, 100)
    random_number2 = randint(1, 100)
    operator = choice(['+', '-', '*'])
    print(f'Question: {random_number1} {operator} {random_number2}')
    correct_unswer = calculate(random_number1, random_number2, operator)
    return correct_unswer


if __name__ == '__main__':
    main()