#starting at 10h43 31/08/2021
#first update at 12h19 31/08/2021


size = int(input("chose the size of the star (1, 2, 3, ...)\n"))


rows = size * 4 + 1
cols = size * 6 + 1
board = [[' ' for i in range(cols)] for j in range(rows)]

midle_cols = int(size * 6 / 2)
last_rows = rows - 1

board[0][midle_cols] = '*'
board[last_rows][midle_cols] = '*'

x = 0
y = last_rows
chars_left = midle_cols
chars_right = midle_cols

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

while chars_left < size + 1 :
    board[x][chars_left] = '*'
    board[y][chars_left] = '*'
    board[x][chars_right] = '*'
    board[y][chars_right] = '*'
    x += 1
    y -= 1
    chars_right -= 1
    chars_left += 1

print('________________________________________')
print(f"chars left :{chars_left}")
print(f"chars right :{chars_right}")
print(f"x :{x}")
print(f"y :{y}")
print('________________________________________\n')


for i in range(len(board)):
    for j in range(len(board[i])):
        print(board[i][j], end='')
    print()
 