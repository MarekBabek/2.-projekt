"""

projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Marek Bábek

email: marek.babek@centrum.cz

discord: Pixoun #0920

"""

import functions_tictactoe as fncts

# Vlastní proměnné
the_field = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
valid_moves = [0, 1, 2, 3, 4, 5, 6, 7, 8]
player = 'X'
move_count = 0
winner = False

# Funkce: Pozdravení uživatele + Vypsání instrukcí hry + Hrací plocha
fncts.display_instructions()

# While smyčka hry:
while not winner:
    # funkce zobrazení aktuální hrací plochy
    fncts.print_playing_field(the_field)
    print(f'It\'s your turn: {player}')

    # Zadání čísla uživatelem po místo v hracím poli
    player_choice = input('Pick a number (1-9) for your mark: ')

    # Pokračuj dále, pokud uživatel zadal číslo ve stringu, následné přemapování na integer
    if player_choice.isdigit():
        player_choice = int(player_choice)

        # Posunutí čísla od uživatele o jedno méně
        # uživatel zadá 1, přemapuje se na index 0 v proměnné the_field
        player_choice -= 1

        # Pokračuj dále, pokud uživatel zadal číslo od 1 do 9
        if player_choice in valid_moves:

            # Pokud číslo uživatele se shoduje neobsazenému indexu v hracím poli, tak doplň znak příslušného hráče
            if the_field[player_choice] == ' ':
                the_field[player_choice] = player
                move_count += 1

                # Pokud jsou 3 znaky stejného hráče v dané rovině
                # zobrazí hrací pole + vypíše vítěze + ukončí program
                # Horizontální vítěz (1. řada)
                if the_field[0] == the_field[1] == the_field[2] != ' ':
                    fncts.blank_space()
                    print_playing_field(the_field)
                    print(f'The winner is {player}')
                    break
                # Horizontální vítěz (2. řada)
                elif the_field[3] == the_field[4] == the_field[5] != ' ':
                    fncts.blank_space()
                    fncts.print_playing_field(the_field)
                    print(f'The winner is {player}')
                    break
                # Horizontální vítěz (3. řada)
                elif the_field[6] == the_field[7] == the_field[8] != ' ':
                    fncts.blank_space()
                    fncts.print_playing_field(the_field)
                    print(f'The winner is {player}')
                    break
                # Vertikální vítěz (levý sloupec)
                elif the_field[0] == the_field[3] == the_field[6] != ' ':
                    fncts.blank_space()
                    fncts.print_playing_field(the_field)
                    print(f'The winner is {player}')
                    break
                # Vertikální vítěz (středový sloupec)
                elif the_field[1] == the_field[4] == the_field[7] != ' ':
                    fncts.blank_space()
                    fncts.print_playing_field(the_field)
                    print(f'The winner is {player}')
                    break
                # Vertikální vítěz (pravý sloupec)
                elif the_field[2] == the_field[5] == the_field[8] != ' ':
                    fncts.blank_space()
                    fncts.print_playing_field(the_field)
                    print(f'The winner is {player}')
                    break
                # Vítěz úhlopříčky (levý spodní roh až pravý horní roh
                elif the_field[0] == the_field[4] == the_field[8] != ' ':
                    fncts.blank_space()
                    fncts.print_playing_field(the_field)
                    print(f'The winner is {player}')
                    break
                # Vítěz úhlopříčky (pravý spodní roh až levý horní roh
                elif the_field[2] == the_field[4] == the_field[6] != ' ':
                    fncts.blank_space()
                    fncts.print_playing_field(the_field)
                    print(f'The winner is {player}')
                    break

                # Funkce: Pokud hřáč správně odehraje svůj tah, tak pokračuje hráč další
                player = fncts.change_player(player)

            # Pokud je místo v hracím poli obsazené
            # upozorni a umožni zadávat znovu + vypsání instrukce obsazení hracího pole
            else:
                fncts.blank_space()
                fncts.displayed_field()
                print('\033[0;31mWarning: \033[00m', 'Spot is already filled')
                print('Above Warning is displayed field, choose empty spot')
                continue
        # Pokud uživatel zadal jiné číslo než čísla 1-9 (upozorní a umožni zadávat znovu)
        else:
            fncts.blank_space()
            print('\033[0;31mWarning: \033[00m', 'Wrong input, try again')
            continue
    # Pokud uživatel zadá cokoliv jiného než číslo (upozorni a umožni zadávat znovu)
    else:
        fncts.blank_space()
        print('\033[0;31mWarning: \033[00m', 'Only numbers in range 1-9 are allowed')
        continue

    # Pokud je hrací pole plné a nikdo nevyhrál, vypíše finální hrací pole + upozorní na remízu
    if move_count == 9:
        fncts.blank_space()
        print('\033[0;31mWarning: \033[00m', 'GAME OVER')
        fncts.print_playing_field(the_field)
        print('It\'s a tie')
        break