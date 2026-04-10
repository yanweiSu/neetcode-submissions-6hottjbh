class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [[0] * 9 for _ in range(9)]
        col = [[0] * 9 for _ in range(9)]
        block = [[0] * 9 for _ in range(9)]
        ### (i,j): the ith row/col/block, value j's count

        for i in range(9):
            for j in range(9):
                if board[i][j].isdigit():
                    val = int(board[i][j]) - 1
                    row[i][val] += 1
                    if row[i][val] > 1:
                        return False
                    col[j][val] += 1
                    if col[j][val] > 1:
                        return False

                    # block's index: (i//3) * 3 + (j//3)
                    block[(i//3) * 3 + (j//3)][val] += 1
                    if block[(i//3) * 3 + (j//3)][val] > 1:
                        return False

        return True