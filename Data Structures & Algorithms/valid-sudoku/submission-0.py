class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #make 9 rows that don't contain duplicates
        rows = [set() for _ in range(9)]
        #make 9 cols that don't contain duplicates
        cols = [set() for _ in range(9)]
        #make 9 squares that don't contain duplicates
        squares = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                num = board[r][c]

                if num == ".":
                    continue

                #The * 3 is necessary because each row of boxes contains 3 boxes.
                square = (r // 3) * 3 + (c // 3)

                if (num in rows[r] or
                    num in cols[c] or
                    num in squares[square]):
                    return False

                rows[r].add(num)
                cols[c].add(num)
                squares[square].add(num)

        return True