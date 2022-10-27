from random import randint
import prompt


def welcome_user():
    print("Welcome to the Brain Games!")
    player_name = prompt.string('May I have your name? ')
    print(f'Hello, {player_name}!')
    return (player_name)


def even_logic():
    random_number = randint(1, 1000)
    print(f'Question: {random_number}')
    player_unswer = prompt.string('Your answer: ')
    correct_unswer = random_number % 2 == 0 and 'yes' or 'no'
    is_correct = correct_unswer == player_unswer
    if not is_correct:
        print(f"'{player_unswer}' is wrong answer ;(. "
                    f"Correct answer was '{correct_unswer}'.")
    return (is_correct)


def main():
    play_times = 3
    player_name = welcome_user()
    print ('Answer "yes" if the number is even, otherwise answer "no".')
    for i in range(0, play_times):
        is_correct = even_logic()
        if not is_correct:
            print(f"Let's try again, {player_name}!")
            return
        print("Correct!")
    print(f"Congratulations, {player_name}!")



if __name__ == '__main__':
    main()