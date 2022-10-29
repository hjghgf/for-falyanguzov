import time


endgame = False
x = time.time_ns()
a = 141
c = 28411
m = 134456


def is_num_correct(num):
    num = str(num)
    if not len(num) == 4 or not len(set(num)) == 4:
        return False
    return True


def generate_secret():
    global x, a, m, c
    x = (a * x + c) % m
    if not is_num_correct(x):
        generate_secret()
    return x


def inp():
    while True:
        print('exit, guess')
        s = input()
        if s.startswith('exit'):
            print('bye')
            raise SystemExit
        if s.startswith('guess '):
            s = s[len('guess '):]
        s = s.strip()
        if not s.isdigit():
            print('должны быть только цифры')
            continue
        elif not len(s) == 4:
            print('длина должна быть 4')
            continue
        elif not len(set(s)) == 4:
            print('все цифры должны быть разные')
            continue
        break
    return s


def main_game(new, right_num):
    bulls = 0
    cows = 0
    for i in range(4):
        if new[i] == right_num[i]:
            bulls += 1
        else:
            for n in range(4):
                if new[n] == right_num[i] and n != i:
                    cows += 1
    if bulls == 4:
        global endgame
        print('ураура победа, пака')
        endgame = True
    else:
        print('быков -', bulls, ', коров -', cows)


right_number = str(generate_secret())
while not endgame:
    new_num = inp()
    main_game(new_num, right_number)
