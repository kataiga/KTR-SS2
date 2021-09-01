#starting at 10h43 31/08/2021
#first update at 12h19 31/08/2021


size = int(input("chose the size of the star (1, 2, 3, ...)\n"))
if size != 0:

    #creating the board
    rows = size * 4 + 1
    cols = size * 6 + 1
    board = [[' ' for i in range(cols)] for j in range(rows)]

    middle_cols = int(size * 6 / 2)
    last_rows = rows - 1
    board[0][middle_cols] = '*'
    board[last_rows][middle_cols] = '*'

    #var setup
    x = 0
    y = last_rows
    chars_left = middle_cols
    chars_right = middle_cols

    #draw the top and botom part of the star
    for n in range(size - 1):
        chars_right += 1
        chars_left -= 1
        x += 1
        y -= 1
        board[x][chars_right] = '*'
        board[x][chars_left] = '*'
        board[y][chars_right] = '*'
        board[y][chars_left] = '*'

    x += 1
    y -= 1
    chars_right += 1
    chars_left -= 1

    #draw the horizontal line
    while chars_left > -1:
        board[x][chars_left] = '*'
        board[y][chars_left] = '*'
        chars_left -= 1

        board[x][chars_right] = '*'
        board[y][chars_right] = '*'
        chars_right += 1

    x += 1
    y -= 1
    chars_right -= 2
    chars_left += 2

    #draw the middle part of the star
    while chars_left < size + 1 :
        board[x][chars_left] = '*'
        board[y][chars_left] = '*'
        board[x][chars_right] = '*'
        board[y][chars_right] = '*'
        x += 1
        y -= 1
        chars_right -= 1
        chars_left += 1

    #display the board corectly
    for i in range(len(board)):
        for j in range(len(board[i])):
            print(board[i][j], end='')
        print()