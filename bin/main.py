import sys
from colorama import Fore,Style

def new_board():
  #return a new board state
  return [[None for i in range(3)] for i in range(3)]

def render(board):
  display_states = {
    None: " ",
    "X": Fore.GREEN + "X",
    "O": Fore.YELLOW + "O"
  }

  lines = []
  print(Fore.LIGHTWHITE_EX + "   0 1 2 ")
  print(Fore.LIGHTWHITE_EX + "  ------- ")
  for k,row in enumerate(board):
    line = Fore.LIGHTWHITE_EX + str(k)+"|"
    for col in row:
      line += " " + display_states[col]
    line += Fore.LIGHTWHITE_EX + " |"
    lines.append(line)
  print("\n".join(lines))
  print(Fore.LIGHTWHITE_EX + "  ------- ")
  print(Style.RESET_ALL)


def get_move():
  x_coord = input("What is your move's X co-ordinate?: ")
  y_coord = input("What is your move's Y co-ordinate?: ")

  if int(x_coord) < 0 or int(x_coord) > 2 or int(y_coord) < 0 or int(y_coord) > 2:
    print("Error: Invalid input! Co-ordinates must have a value between 0 and 2.")
    sys.exit(0)

  return (x_coord, y_coord)

def is_valid_move(board, coordinates):
  x_coord = int(coordinates[0])
  y_coord = int(coordinates[1])
  
  if board[x_coord][y_coord] is not None:
    print("Error! Can't make move ({},{}), square already taken!".format(coordinates[0], coordinates[1]))
    sys.exit(0)

  return True

def make_move(board, coordinates, user_move):

  is_valid_move(board ,coordinates)

  x_coord = int(coordinates[0])
  y_coord = int(coordinates[1])

  board[x_coord][y_coord] = user_move


def get_coord_count():
  rows = []
  for i in range(0,3):
    row = []
    for j in range(0,3):
      row.append((i,j))
    rows.append(row)

  cols = []
  for i in range(0,3):
    col = []
    for j in range(0,3):
      col.append((j,i))
    cols.append(col)

  diagonals = [
    [(0, 0), (1, 1), (2, 2)],
    [(0, 2), (1, 1), (2, 0)]
  ]

  return rows + cols + diagonals

  

def has_winner(board):
  grouped_coords = get_coord_count()

  for line in grouped_coords:
    board_values = []
    for (x,y) in line:
      board_values.append(board[x][y])
    if len(set(board_values)) == 1 and board_values[0] is not None:
        return board_values[0]

  return None


def is_board_full(board):
  for row in board:
    for col in row:
      if col is None:
        return False
  
  return True


def main():

  user_0 = input("Enter Player 1's name: ")
  user_1 = input("Enter Player 2's name: ")

  print("Player 1 will use X")
  print("Player 2 will use O")

  user_player_map = {
    "X": user_0,
    "O": user_1
  }

  allowed_states = [
    "X",
    "O"
  ]

  player_id = 0

  board = new_board()

  move_coords = None

  while True:

    render(board)
    move_coords = get_move()

    user_move = allowed_states[player_id % 2]

    make_move(board, move_coords, user_move)

    winner = has_winner(board)
    if winner:
      render(board)
      print(Fore.GREEN + "The WINNER is {}!".format(user_player_map[winner]))
      break

    if is_board_full(board):
      render(board)
      print(Fore.MAGENTA + "It is a DRAW!")
      break

    player_id += 1
  
  print(Style.RESET_ALL)


if __name__ == "__main__":
    main()