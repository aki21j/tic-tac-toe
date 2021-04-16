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

  
def get_all_available_moves(board):
  legal_moves = []
  for x, row in enumerate(board):
    for y, val in enumerate(row):
      if val is None:
        legal_moves.append((x, y))
  return legal_moves