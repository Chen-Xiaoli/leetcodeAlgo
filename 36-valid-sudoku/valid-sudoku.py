class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [[0] * 9 for _ in range(9)]
        cols = [[0] * 9 for _ in range(9)]

        subboxes = [[[0] * 9 for _ in range(3)] for _ in range(3)]

        for i in range(9):
            for j in range(9):
                c = board[i][j]
                if c != '.':
                    c = int(c) - 1
                    rows[i][c] += 1
                    cols[j][c] += 1
                    subboxes[int(i/3)][int(j/3)][c] += 1

                    if rows[i][c] > 1 or cols[j][c] > 1 or  subboxes[int(i/3)][int(j/3)][c] > 1:
                        return False
        return True