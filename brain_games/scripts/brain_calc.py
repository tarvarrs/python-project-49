#!/usr/bin/env python3
from random import randint, choice
import brain_games.games.logics as logics


def main():
    name = logics.greet_user()
    res = 0
    print('What is the result of the expression?')

    while True:
        a = randint(10, 50)
        b = randint(0, 10)
        operation = choice(['+', '-', '*'])

        match operation:
            case '+':
                correct_ans = a + b
            case '-':
                correct_ans = a - b
            case '*':
                correct_ans = a * b

        print(f'Question: {a} {operation} {b}')
        ans = logics.make_decimal(logics.get_answer())

        if isinstance(ans, int) and logics.is_answer_correct(ans, correct_ans):
            res += 1

            if logics.is_win(res):
                logics.win_message(name)
                break
        else:
            logics.loose_message(ans, correct_ans, name)
            break


if __name__ == '__main__':
    main()
