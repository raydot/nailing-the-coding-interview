def check_board(board):
    return check_rows(board) and check_columns(board) and check_diagonals(board) and check_anti_diagonals(board)

# def check_board(board):
#     rows = check_rows(board)
#     cols = check_columns(board)
#     diags = check_diagonals(board)
#     anti_diags = check_anti_diagonals(board)
    
#     print(f"Rows check: {rows}")
#     print(f"Columns check: {cols}")
#     print(f"Diagonals check: {diags}")
#     print(f"Anti-diagonals check: {anti_diags}")
    
#     return rows and cols and diags and anti_diags

def check_rows(board):
    for row in board:
        if row.count(1) != 1:
            return False
    return True

def check_columns(board):
    num_rows = len(board)
    num_cols = len(board[0])
    
    for col in range(num_cols):
        count = 0
        for row in range(num_rows):
            if board[row][col] == 1:
                count += 1
        if count != 1:
            return False
    return True

def check_diagonals(board):
    num_rows = len(board)
    num_cols = len(board[0])
    
    for start in range(num_rows + num_cols - 1):
        count = 0
        for i in range(max(0, start - num_cols + 1), min(num_rows, start + 1)):
            if board[i][start - i] == 1:
                count += 1
        if count > 1: # There's more than one queen in the diagonal!
            return False
    return True
  
def check_anti_diagonals(board):
    num_rows = len(board)
    num_cols = len(board[0])
    
    for start in range(num_rows + num_cols - 1):
        count = 0
        for i in range(max(0, start - num_cols + 1), min(num_rows, start + 1)):
            j = num_cols - 1 - (start - i)
            if 0 <= j < num_cols and board[i][j] == 1:
                count += 1
        if count > 1: 
            return False
    return True
  
# Valid board - one queen per row, column, and diagonal
valid_board = [
    [0, 1, 0, 0],
    [0, 0, 0, 1],
    [1, 0, 0, 0],
    [0, 0, 1, 0]
]

# Invalid board - queens can attack each other
invalid_board = [
    [1, 0, 0, 0],
    [0, 0, 0, 1],
    [0, 0, 1, 0],
    [0, 1, 0, 0]
]

# Test the boards
print("Valid board result:", check_board(valid_board))    # Should print True
print("Invalid board result:", check_board(invalid_board))  # Should print False