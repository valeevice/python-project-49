from random import randint
from random import choice
import operator
import prompt


get_operator = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
}.get 


def calculate(x, y, operator):
    op = get_operator(operator)
    return (op(x, y))


def welcome_user():
    print("Welcome to the Brain Games!")
    player_name = prompt.string('May I have your name? ')
    print(f'Hello, {player_name}!')
    return (player_name)


def calc_logic():
    random_number1 = randint(1, 100)
    random_number2 = randint(1, 100)
    operator = choice(['+', '-', '*'])
    print(f'Question: {random_number1} {operator} {random_number2}')
    player_unswer = prompt.string('Your answer: ')
    correct_unswer = calculate(random_number1, random_number2, operator)
    is_correct = str(correct_unswer) == player_unswer
    if not is_correct:
        print(f"'{player_unswer}' is wrong answer ;(. "
                    f"Correct answer was '{correct_unswer}'.")
    return (is_correct)



def main():
    play_times = 3
    player_name = welcome_user()
    print ('What is the result of the expression?')
    for i in range(0, play_times):
        is_correct = calc_logic()
        if not is_correct:
            print(f"Let's try again, {player_name}!")
            return
        print("Correct!")
    print(f"Congratulations, {player_name}!")



if __name__ == '__main__':
    main()