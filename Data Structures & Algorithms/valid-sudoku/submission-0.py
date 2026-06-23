class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Naala solution
        # n = len(board)
        # for i in range(n):
        #     for j in range(n):
        #         for k in range(n):# for vertical and horizontal
        #             if board[i][j] ==board[k][j] and board[i][j] == board[i][k]:
        #                 return False
        #         #subgrid:
        #         start_x, start_y = int(i/3)*3, int(i/3)*3
        #         print(start_x,start_y)
        #         end_x, end_y = start_x+3, start_x+3
        #         for x in range(start_x,end_x):
        #             for y in range(start_y,end_y):
        #                 if board[i][j] ==board[x][y]:
        #                     return False
        # return True
        #True Solution:
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        square = collections.defaultdict(set)
        
        for row in range(9):
            for col in range(9):
                if board[row][col] == '.':
                    continue
                if (board[row][col] in rows[row]
                    or board[row][col] in cols[col]
                    or board[row][col] in square[row//3,col//3]
                    ): 
                    return False
                rows[row].add(board[row][col])
                cols[col].add(board[row][col])
                square[row//3,col//3].add(board[row][col])

        return True