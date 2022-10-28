from brain_games import f_m
from brain_games.games import logic_even
from brain_games.games import logic_calc

def task_of_game(name_game):
    if name_game == "brain_even":
        print ('Answer "yes" if the number is even, otherwise answer "no".')
    if name_game == "brain_calc":
        print ('What is the result of the expression?')
    

def get_unswer(name_game):
    if name_game == "brain_even":
        return(logic_even.question_unswer())
    if name_game == "brain_calc":
        return(logic_calc.question_unswer())



def any_game(name_game):
    player_name = f_m.welcome_user()
    task_of_game(name_game)
    for i in range(0, f_m.AMOUNT_GAMES):
        correct_unswer = get_unswer(name_game)
        player_unswer = f_m.unswer()
        if not f_m.is_correct(player_unswer, correct_unswer):
            print(f"Let's try again, {player_name}!")
            return
        print("Correct!")
    print(f"Congratulations, {player_name}!")
    return