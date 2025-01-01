import pandas as pd

print('PLAYER INFO: ')
print('------------------------------------------------------------------\n')
ef = pd.read_csv('player_detail.csv')
print(ef)

tic_tac_toe_board = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
                     'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
                     'bot-L': ' ', 'bot-M': ' ', 'bot-R': ' ', }


def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['bot-L'] + '|' + board['bot-M'] + '|' + board['bot-R'])


move: str = 'X'

def _store(x):
    #Horizontaly equal:

    if \
            x['top-L'] == x['top-M'] == x['top-R'] == move:
        print(f'{move} has won')
        raise StopIteration


    elif \
            x['mid-L'] == x['mid-M'] == x['mid-R'] == move:
        print(f'{move} has won')
        raise StopIteration


    elif \
            x['bot-L'] == x['bot-M'] == x['bot-R'] == move:
        print(f'{move} has won')
        raise StopIteration

    #Vertically equal:

    elif \
            x['top-L'] == x['mid-L'] == x['bot-L'] == move:
        print(f'{move} has won')
        raise StopIteration

    elif \
            x['top-M'] == x['mid-M'] == x['bot-M'] == move:
        print(f'{move} has won')
        raise StopIteration


    elif \
            x['top-R'] == x['mid-R'] == x['bot-R'] == move:
        print(f'{move} has won')
        raise StopIteration

    #Diagonally equal:

    elif \
            x['top-L'] == x['mid-M'] == x['bot-R'] == move:
        print(f'{move} has won')
        raise StopIteration


    elif \
            x['top-R'] == x['mid-M'] == x['bot-R'] == move:
        print(f'{move} has won')
        raise StopIteration


_count = 0
try:
    while True:
        if _count == 9:
            break
        else:
            m: str = input(f'Enter move {move}: ')
            if m not in tic_tac_toe_board:
                print('ERROR!!')



            else:
                if tic_tac_toe_board.get(m) != ' ':
                    print('Already used !!')

                else:
                    tic_tac_toe_board[m] = move
                    _store(tic_tac_toe_board)
                    printBoard(tic_tac_toe_board)
                    _count += 1
                    if move == 'X':
                        move = 'O'
                    else:
                        move = 'X'

except StopIteration:
    print('Game Over!')