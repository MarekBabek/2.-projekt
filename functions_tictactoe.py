def display_instructions():
    print(
        '''
        Welcome to Tic Tac Toe game
        ========================================
        GAME RULES:
        Each player can place one mark (or stone)
        per turn on the 3x3 grid. The WINNER is
        who succeeds in placing three of their
        marks in a:
        * horizontal,
        * vertical or
        * diagonal row

        Displayed playing field, same as your numeric keyboard:
         ───────────
        | 7 | 8 | 9 |
        |---+---+---|
        | 4 | 5 | 6 |
        |---+---+---|
        | 1 | 2 | 3 |
         ───────────
        ========================================
        '''
        )

def displayed_field():
    print(
        '''
         ───────────
        | 7 | 8 | 9 |
        |---+---+---|
        | 4 | 5 | 6 |
        |---+---+---|
        | 1 | 2 | 3 |
         ───────────
         ''')

def blank_space():
    print('')

def print_playing_field(field):
    print('', u'\u2500' * 11, '')
    print('|', field[6], '|', field[7], '|', field[8], '|')
    print('|' + '---' + '+' + '---' + '+' + '---' + '|')
    print('|', field[3], '|', field[4], '|', field[5], '|')
    print('|' + '---' + '+' + '---' + '+' + '---' + '|')
    print('|', field[0], '|', field[1], '|', field[2], '|')
    print('', u'\u2500' * 11, '')

def change_player(player):
    if player == 'X':
        return 'O'
    else:
        return 'X'