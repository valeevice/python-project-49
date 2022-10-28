from random import randint


def question_unswer():
    # n1 + b
    n1 = randint(1, 100)
    b = randint(1, 20)
    len_progression = randint(5, 15)
    unknown_count = randint(0, len_progression - 1)
    progression = []
    for i in range(0, len_progression):
        if i == unknown_count:
            correct_unswer = str(n1 + b * i)
            progression.append("..")
        else:
            progression.append(str(n1 + b * i))
    print(f'Question: {" ".join(progression)}')
    return str(correct_unswer)
