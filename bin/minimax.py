from main import make_move, has_winner, is_board_full
from utils import get_opponent, get_all_available_moves
import copy

cache = {}

def _minimax_score(board, player_to_move, current_player):
  cache_key = str(board)

  if cache_key not in cache:
    score = minimax_score(board, player_to_move, current_player)

    cache[cache_key] = score

  return cache[cache_key]


def minimax_score(board, player_to_move, current_player):

  winner = has_winner(board)
  if winner is not None:
    if winner == current_player:
      return 10
    else:
      return -10
  elif is_board_full(board):
    return 0

  legal_moves = get_all_available_moves(board)

  scores = []
  for move in legal_moves:
    # First make the move
    if move == None:
      continue
    _board = copy.deepcopy(board)
    make_move(_board, move, player_to_move)

    opponent = get_opponent(player_to_move)
    score = minimax_score(_board, opponent, current_player)
    scores.append(score)

  if player_to_move == current_player:
    return max(scores)
  else:
    return min(scores)


def minimax_ai(board, player_state):
  best_move = None
  best_score = None

  legal_moves = get_all_available_moves(board)

  for move in legal_moves:
    _board = copy.deepcopy(board)

    make_move(_board, move, player_state)

    opp = get_opponent(player_state)

    score = _minimax_score(_board, opp, player_state)

    if best_score is None or score > best_score:
      best_move = move
      best_score = score


  return best_move