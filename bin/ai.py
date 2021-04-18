import random
from utils import get_all_available_moves, get_coord_count


def finds_winning_moves_ai(board, player_state):
  winning_move = get_winning_move(board, player_state)
  if winning_move:
    return winning_move
  
  return random_move(board)

def blocks_winning_moves_ai(board, player_state, block_state):
  to_block = get_winning_move(board, block_state)
  winning_move = get_winning_move(board, player_state)

  if to_block:
    return to_block
  elif winning_move:
    return winning_move
  
  return random_move(board)

def get_winning_move(board, player_state):
  grouped_coords = get_coord_count()

  for line in grouped_coords:
    player_count = 0
    player_next = 0
    next_coord = None

    for (x,y) in line:
      val = board[x][y]
      if val == player_state:
        player_count += 1
      elif val == None:
        player_next += 1
        next_coord = (x,y)

    if player_count == 2 and player_next == 1:
      return next_coord


def random_move(board):
  available_moves = get_all_available_moves(board)
  return random.choice(available_moves)
