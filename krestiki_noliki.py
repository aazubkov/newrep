# -------------------------
# defining functions
# -------------------------

# printing Hello and description of the game
def print_hello():
    print('-' * 40)
    print('Hello, dear strangers! \nThis is Krestiki vs Noliki Battle! '
          '\nYour have to choose the side and do your best to defeat the enemy!'
          '\nPlayers need to enter coordinates of each turn in XY-format. Rules are simple.'
          '\nWinner is the side which collects row or column or any diagonals with 3 same figures (X or O)'
          '\nSo let the Battle started!!!')
    print('-' * 40, '\n')

# printing matrix field
def print_field():
    for i in mtx:
        print(*i, sep = ' | ', end = '')
        print(' |  (x→)' if i == mtx[0] else ' | ')         # comment X axis with x→
        print('-' * 15)
    print('(y↓)')                                           # comment Y axis with y↓

# asking for players' names:
def ask_names():
    return input('Player Cross, input your name: '), input('Player Zero, input your name: ')

# asking the player for coordinates
def ask_turn(pl):
    flag = False
    while not flag:
        inp_hod = input(f"{pl}, it's your turn. Enter coordinates in X Y format: -> ")
        if ' ' in inp_hod:
            y, x = inp_hod.split(' ', 1)
        else:
            print('ERROR: spaces between coordinates are not correct.')
            continue
        flag = check_turn_correct(x, y)         # checking if input was correct
    return(int(x), int(y))


# checking if turn's input is correct
# 1) general checking
def check_turn_correct(x, y):
    return check_digit(x, y) and check_range(x, y) and check_free_area(x, y)

# 2) checkin if these are digits
def check_digit(x, y):
    if x.isdigit() and y.isdigit():
        return True
    else:
        print(f'ERROR: not digits or too many spaces in "{y}"!')
        return False

# 3) checking if coordinates are in field range
def check_range(x, y):
    x, y = int(x), int(y)
    if 1 <= x <= 3 and 1 <= y <= 3:
        return True
    else:
        print('ERROR: coordinates are not on the field, man!')
        return False

# 4) checking if pointed coordinates are free and not occupied by X/O
def check_free_area(x, y):
    x, y = int(x), int(y)
    if mtx[x][y] == probel:
        return True
    else:
        print(f'ERROR: this place is already taken by {mtx[x][y]}')
        return False

# imputing turn coordinates with X or O into the matrix field (actually useless function with 1 command) :
def make_turn(x, y, fig):
    mtx[x][y] = fig

# checking if game ends with the victory
def check_victory(hod):
    win_list = [fig[hod % 2]] * 3  # defining the Winning list of [X X X] or [O O O] - depends on whose turn it was
    # checking rows
    for mtxi in mtx:
        if mtxi[1:] == win_list:
            return True

    # checking columns
    for j in range(1, 4):
        col_list = []
        for i in range(1, 4):
            col_list.append(mtx[i][j])
        if col_list == win_list:
            return True

    # checking both diagonals
    col_list = []
    for i in range(1, 4):
        col_list.append(mtx[i][i])
    if col_list == win_list:
        return True
    col_list = []
    for i in range(1, 4):
        col_list.append(mtx[4 - i][i])
    if col_list == win_list:
        return True
    return False

# checking if game ends
def check_game_end(hod):
    if check_victory(hod):  # checking if game ends with the VICTORY
        print(f'OMG!! Here we have a winner!! Ole ole ole! {player[hod % 2]} wins!! Our congrats! You are the BOSS!')
        return True
    if hod == 8:            # checking if game ends with DRAW because of 9 turns made
        print("No more turns. That's over, folks! Game has finished with DRAW. Nichya, muzhinki!")
        return True
    return False


# -------------------------
# main code
# -------------------------
probel = ' '            # instead of space any symbol can be used
fig = ('X', 'O')        # define figures XO tuple

play_new_game_flag = True
while play_new_game_flag:
    # create matrix field with col and row numbers
    # I decided mtx list to keep global
    mtx = [[probel for _ in range(4)] for _ in range(4)]    # filling 4 x 4 matrix with probel
    mtx[0] = [i for i in range(4)]                          # first row is coordinates of X-axis
    for i in range(4):                                      # first column is coordinates of Y-axis
        mtx[i][0] = i
    mtx[0][0] = ' '                                          # left upper conner let be empty

    print_hello()           # print description of the game
    player = ask_names()    # asking for input player names
    print_field()           # printing matrix field

    hod = 0                 # counting of turns
    game_flag = True
    while game_flag:        # while flag is True game is continuing
        x, y = ask_turn(player[hod % 2])            # define x, y coordinates of next turn (correction is checked inside)
        make_turn(x, y, fig[hod % 2])               # updating matrix field with the turn coordinates
        print_field()                               # printing matrix field
        game_flag = not check_game_end(hod)         # checking if games finishes with DRAW or WIN (if so, printing results)
        hod += 1                                    # increasing of turn +1
    print()
    ans = ''
    while ans != 'Y' and ans != 'N':
        ans = input('Play once more? "Y" - yes, need a return match. "N" - no, I am the BOSS!  -->')
        play_new_game_flag = True if ans == 'Y' else False
s