import sys
from colorama import Fore,Style
import ai
from utils import get_coord_count

AVAILABLE_GAME_MODES = {
  "RANDOM_CHOICE_AI": "RANDOM_CHOICE_AI",
  "WINNING_MOVE_AI": "WINNING_MOVE_AI",
  "TWO_PLAYER": "TWO_PLAYER"
}

allowed_states = [
  "X",
  "O"
]

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


def get_human_moves():
  x_coord = input("What is your move's X co-ordinate?: ")
  y_coord = input("What is your move's Y co-ordinate?: ")

  if int(x_coord) < 0 or int(x_coord) > 2 or int(y_coord) < 0 or int(y_coord) > 2:
    print("Error: Invalid input! Co-ordinates must have a value between 0 and 2.")
    sys.exit(0)

  return (x_coord, y_coord)

def get_move(board, mode, player_id):

  if player_id % 2 != 0:
    if mode == AVAILABLE_GAME_MODES["RANDOM_CHOICE_AI"]:
      return ai.random_move(board)
    elif mode == AVAILABLE_GAME_MODES["WINNING_MOVE_AI"]:
      return ai.finds_winning_moves_ai(board, allowed_states[player_id % 2])
  elif mode == AVAILABLE_GAME_MODES["TWO_PLAYER"] or player_id % 2 == 0:
    return get_human_moves()


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

def select_mode():
  user_inp = input("Enter 0 for Random choice AI,1 for Winning Moves AI and 2 for Two player mode: ")

  if int(user_inp) > 2:
    print("Invalid input! Please enter a valid input!")
    sys.exit(0)
  if int(user_inp) == 0:
    return AVAILABLE_GAME_MODES["RANDOM_CHOICE_AI"]
  elif int(user_inp) == 1:
    return AVAILABLE_GAME_MODES["WINNING_MOVE_AI"]
  else:
    return AVAILABLE_GAME_MODES["TWO_PLAYER"]


def main():

  selected_mode = select_mode()
  user_0 = input("Enter Player 1's name: ")
  user_1 = "Zelda"

  print(selected_mode)

  if selected_mode == AVAILABLE_GAME_MODES["TWO_PLAYER"]:
    user_1 = input("Enter Player 2's name: ")

  print("Player 1 will use X")
  print("Player 2 will use O")

  user_player_map = {
    "X": user_0,
    "O": user_1
  }

  player_id = 0

  board = new_board()

  move_coords = None

  while True:

    render(board)
    user_move = allowed_states[player_id % 2]

    move_coords = get_move(board, selected_mode, player_id)

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