#!/usr/bin/env python3
from random import randint
import brain_games.games.logics as logics


def main():
    name = logics.greet_user()
    res = 0
    print('What number is missing in the progression?')

    while True:
        prog = generate_progression()
        correct_ans, question_progression = hide_element_in_progression(prog)
        print(f'Question: {question_progression}')
        ans = logics.make_decimal(logics.get_answer())

        if isinstance(ans, int) and logics.is_answer_correct(ans, correct_ans):
            res += 1

            if logics.is_win(res):
                logics.win_message(name)
                break
        else:
            logics.loose_message(ans, correct_ans, name)
            break


def generate_progression():
    progression_length = randint(5, 10)
    current_number = randint(0, 30)
    step = randint(1, 5)
    progression = []
    i = progression_length

    while i:
        progression.append(current_number)
        current_number += step
        i -= 1

    return progression


def hide_element_in_progression(progression):
    hide_index = randint(0, len(progression) - 1)
    hidden_element, progression[hide_index] = progression[hide_index], '..'

    return (hidden_element, progression)


if __name__ == '__main__':
    main()
