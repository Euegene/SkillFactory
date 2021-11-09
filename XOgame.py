board = list(range(1, 10))

win_archive = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7)]


def drawing_board():
    print('-------------')
    for i in range(3):
        print('|', board[0 + i * 3], '|', board[1 + i * 3], '|', board[2 + i * 3], '|')
    print('-------------')


def take_input(player_token):
    while True:
        value = input(f"Введите номер ячейки для {player_token} : ")
        if not (value in '123456789') or len(value) > 1:
            print('Что-то не понятно, пожалуйста повторите: ')
            continue
        value = int(value)
        if str(board[value - 1]) in 'XO':
            print('Увы, эта клетка уже занята. Попробуйте снова')
            continue
        board[value - 1] = player_token
        break


def checking():
    for each in win_archive:
        if (board[each[0] - 1]) == (board[each[1] - 1]) == (board[each[2] - 1]):
            return board[each[1] - 1]
    else:
        return False


def main():
    counter = 0
    while True:
        drawing_board()
        if counter % 2 == 0:
            take_input('X')
        else:
            take_input('O')
        if counter > 3:
            win = checking()
            if win:
                drawing_board()
                print(win, 'одержал победу')
                break
        counter += 1
        if counter == 9:
            drawing_board()
            print('Ничья')
            break


# возник вопрос: как "обнулить" игру?
# Мне хотелось бы задать вопрос "Повторить игру?" через if
# но столкнулась с тем, что вызывается таблица со старыми данными
# это можно как-то исправить?

main()
