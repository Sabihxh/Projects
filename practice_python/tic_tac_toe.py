def tic_tac_box():

    board_size = raw_input('Enter board_size: ')
    board_size = int(board_size)
    board_size_1 = board_size + 1

    for i in range(board_size):
        print(' ---' * board_size)
        print('|   ' * board_size_1)
        
    print(' ---' * board_size)
#tic_tac_box()

def win_or_lose():

    a = [0,0,0]
    b = [a] * 3
    player_1 = 1
    player_2 = 2

    if b[0][0] == b[1][0] == b[2][0]:
        if b[0][0] == 1:
            print("%s won" % player_1)
        elif b[0][0] == 2:
            print("%s won" % player_2)

    if b[0][0] == b[0][1] == b[0][2]:
        if b[0][0] == 1:
            print("%s won" % player_1)
        elif b[0][0] == 2:
            print("%s won" % player_2)

    if b[0][0] == b[1][1] == b[2][2]:
        if b[0][0] == 1:
            print("%s won" % player_1)
        elif b[0][0] == 2:
            print("%s won" % player_2)

    if b[1][0] == b[1][1] == b[1][2]:
        if b[1][0] == 1:
            print("%s won" % player_1)
        elif b[0][0] == 2:
            print("%s won" % player_2)


win_or_lose()













