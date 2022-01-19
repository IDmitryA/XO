from schore_counter import ScoreCounter

str_0 = str_1 = '   |   |   \n---+---+---\n'
str_2 = '   |   |   '
print(str_0 + str_1 + str_2)
field = [list(str_0), list(str_1), list(str_2)]
ScoreCounter.player_1 = input(f'Player 1 enter your name:\n')
ScoreCounter.player_2 = input(f'Player 2 enter your name:\n')
total_score = []


def winner():
    win_comb = [
        [field[0][1] == 'X', field[1][1] == 'X', field[2][1] == 'X'],
        [field[0][5] == 'X', field[1][5] == 'X', field[2][5] == 'X'],
        [field[0][9] == 'X', field[1][9] == 'X', field[2][9] == 'X'],
        [field[0][1] == 'X', field[0][5] == 'X', field[0][9] == 'X'],
        [field[1][1] == 'X', field[1][5] == 'X', field[1][9] == 'X'],
        [field[2][1] == 'X', field[2][5] == 'X', field[2][9] == 'X'],
        [field[0][1] == 'X', field[1][5] == 'X', field[2][9] == 'X'],
        [field[2][1] == 'X', field[1][5] == 'X', field[0][9] == 'X'],
        [field[0][1] == 'O', field[1][1] == 'O', field[2][1] == 'O'],
        [field[0][5] == 'O', field[1][5] == 'O', field[2][5] == 'O'],
        [field[0][9] == 'O', field[1][9] == 'O', field[2][9] == 'O'],
        [field[0][1] == 'O', field[0][5] == 'O', field[0][9] == 'O'],
        [field[1][1] == 'O', field[1][5] == 'O', field[1][9] == 'O'],
        [field[2][1] == 'O', field[2][5] == 'O', field[2][9] == 'O'],
        [field[0][1] == 'O', field[1][5] == 'O', field[2][9] == 'O'],
        [field[2][1] == 'O', field[1][5] == 'O', field[0][9] == 'O']
    ]
    draw = [
        field[0][1] != ' ', field[0][5] != ' ', field[0][9] != ' ',
        field[1][1] != ' ', field[1][5] != ' ', field[1][9] != ' ',
        field[2][1] != ' ', field[2][5] != ' ', field[2][9] != ' '
    ]
    for e in win_comb:
        if all(e):
            total_score.append(current_player)
            print(f'{current_player}, you won')
            return True
        elif all(draw):
            print("It's draw, fellows")
            return True


while True:
    current_player = ScoreCounter.change_current_player()
    ScoreCounter.change_current_player()
    x, y = eval(input(f'{ScoreCounter.change_current_player()}, enter coordinates (x,y):\n'))
    if all([field[3-y][x*3 - (3-x)] == ' ', 0 < x < 4, 0 < y < 4]):
        field[3-y][x*3 - (3-x)] = ScoreCounter.change_mark()
        for i in field:
            b = ''.join(i)
            print(b[:-1:])
        if winner():
            answer = input(f'One more game? - y/n:\n')
            if answer == 'y':
                field[0][1] = field[0][5] = field[0][9] = field[1][1] = field[1][5] = field[1][9] = \
                    field[2][1] = field[2][5] = field[2][9] = ' '
                continue
            else:
                print(f'Total score:\n{ScoreCounter.player_1}:{ScoreCounter.player_2} - '
                      f'{total_score.count(ScoreCounter.player_1)}:{total_score.count(ScoreCounter.player_2)}')
                break

    else:
        print(f'Wrong coordinates. {current_player}, try again!!!')
        ScoreCounter.change_current_player()


