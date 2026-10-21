class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        verticals = [[False for i in range(9)] for i in range(9)]
        horizontals = [[False for i in range(9)] for i in range(9)]
        boxes = [[False for i in range(9)] for i in range(9)]

        for y in range(9):
            for x in range (9):
                num = board[y][x]
                if num != ".":
                    if verticals[y][int(num)-1]:
                        return False
                    else:
                        verticals[y][int(num)-1] = True
                    if horizontals[x][int(num)-1]:
                        return False
                    else:
                        horizontals[x][int(num)-1] = True
                    if boxes[x//3 + 3*(y//3) - 1][int(num)-1]:
                        return False
                    else:
                        boxes[x//3 + 3*(y//3) - 1][int(num)-1] = True
        return True