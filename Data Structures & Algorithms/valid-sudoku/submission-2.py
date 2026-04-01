class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #row check
        for i in range(9):
            rows = set()
            for j in range(9):
                if board[i][j] in rows:
                    return False
                if board[i][j] != ".":
                    rows.add(board[i][j])
        #col check
        for i in range(9):
            cols = set()
            for j in range(9):
                if board[j][i] in cols:
                    return False
                if board[j][i] != ".":
                    cols.add(board[j][i])
        #3x3 check
        starts = [[0,0] , [0,3] , [0,6], [3,0], [3,3], [3,6] , [6,0], [6,3], [6,6]]
        for row, col in starts:
            check = set()
            for i in range(3):
                for j in range(3):
                    if board[row + i][col + j] in check:
                        return False
                    if board[row + i][col + j] != ".":
                        check.add(board[row + i][col + j])
        return True


                
