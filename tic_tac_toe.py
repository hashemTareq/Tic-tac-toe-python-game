import os

player = 'X'
matrix = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]

def display():
  os.system('cls')
  print(' ------------')
  for rows in matrix:
    print(' | ', end='')
    for columns in rows:
      print(f'{columns}  ', end='')
    print('|')
  print(' ------------')


def chage_player():
  global player
  if player == 'X':
    player = 'O'
  else:
    player = 'X'


def user_input():
  position = input(f'Type your position - Plyaer [{player}]: ')[0].strip()
  for rows in matrix:
    for columns in rows:
      if columns == position:
        matrix[matrix.index(rows)][rows.index(columns)] = player
  chage_player()


def determine_winner():
  x_counter, o_counter, game_counter = 0, 0, 0
  for rows in range(0, 3):
    for columns in range(0, 3):
      if (matrix[rows][columns] != 'X' and matrix[rows][columns] != 'O'):
        game_counter += 1
      if matrix[rows][columns] == 'X':
        x_counter += 1
      elif matrix[rows][columns] == 'O':
        o_counter += 1
      if x_counter == 3 or o_counter == 3:
        return 'X' if x_counter > o_counter else 'O'
    x_counter, o_counter = 0, 0

  for rows in range(0, 3):
    for columns in range(0, 3):
      if matrix[columns][rows] == 'X':
        x_counter += 1
      elif matrix[columns][rows] == 'O':
        o_counter += 1
      if x_counter == 3 or o_counter == 3:
        return 'X' if x_counter > o_counter else 'O'
    x_counter, o_counter = 0, 0

    if (matrix[0][0] == 'X' and matrix[1][1] == 'X' and matrix[2][2] == 'X'):
      return 'X'
    elif (matrix[0][0] == 'O' and matrix[1][1] == 'O' and matrix[2][2] == 'O'):
      return 'O'
    elif (matrix[0][2] == 'X' and matrix[1][1] == 'X' and matrix[2][0] == 'X'):
      return 'X'
    elif (matrix[0][2] == 'O' and matrix[1][1] == 'O' and matrix[2][0] == 'O'):
      return 'O'

  if game_counter == 0:
    return 'T'

  return '.'


def play_game():
  while (determine_winner() == '.'):
    display()
    user_input()
  display()
  if determine_winner() == 'T':
    print(' - Game over. Tie!')
  else:
    print(f' - The winner is [{determine_winner()}] player. Congratulations!')


if __name__ == '__main__':
  play_game()
