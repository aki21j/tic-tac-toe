def new_board():
  #return a new board state
  return [[None for i in range(3)] for i in range(3)]

def render(board):
  display_states = {
    None: " ",
    "X": "X",
    "O": "O"
  }

  lines = []
  print("   0 1 2 ")
  print("  ------- ")
  for k,row in enumerate(board):
    line = str(k)+"|"
    for col in row:
      line += " " + display_states[col]
    line += " |"
    lines.append(line)
  print("\n".join(lines))
  print("  ------- ")

def main():
  board = new_board()
  print(board)
  dummy_board = [
    ['X', None, 'O'],
    ['O', None, None],
    [None, 'X', 'X']
  ]
  render(dummy_board)

  # Loop through turns until the game is over
  # loop forever:
  #   # TODO: hmm I'm not sure how best to do this
  #   # right now. No problem, I'll come back later.
  #   current_player = ???

  #   # Print the current state of the board
  #   render(board)

  #   # Get the move that the current player is going
  #   # to make.
  #   move_co_ords = get_move()

  #   # Make the move that we calculated above
  #   make_move(board, move_co_ords, current_player)

  #   # Work out if there's a winner
  #   winner = get_winner(board)

  #   # If there is a winner, crown them the champion
  #   # and exit the loop.
  #   if winner is not None:
  #     print "WINNER IS %s!!" % winner
  #     break

  #   # If there is no winner and the board is full,
  #   # exit the loop.
  #   if is_board_full(board):
  #     print "IT'S A DRAW!!"
  #     break

    # Repeat until the game is over

if __name__ == "__main__":
    main()