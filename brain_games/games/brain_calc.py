from random import randint, choice
import brain_games.logics.logics as logics


def main():
    name = logics.greet_user()
    res = 0

    while True:
        a = randint(0, 10)
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

        ans = logics.get_answer()
        try:
            ans = int(ans)
        except:
            logics.loose_message(ans, correct_ans)
            break

        if isinstance(a, int) and logics.is_answer_correct(ans, correct_ans):
            res += 1
            if logics.is_win(res):
                logics.win_message(name)
                break
        else:
            logics.loose_message(ans, correct_ans)
            break
        
        

if __name__ == '__main__':
    main()
