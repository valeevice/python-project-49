#!/usr/bin/env python3

import prompt

AMOUNT_GAMES = 3

def welcome_user():
    print("Welcome to the Brain Games!")
    player_name = prompt.string('May I have your name? ')
    print(f'Hello, {player_name}!')
    return (player_name)

def unswer():
    player_unswer = prompt.string('Your answer: ')
    return (player_unswer)

def is_correct(player_unswer, correct_unswer):
    if correct_unswer != player_unswer:
        print(f"'{player_unswer}' is wrong answer ;(. "
                    f"Correct answer was '{correct_unswer}'.")
    return (correct_unswer == player_unswer)
