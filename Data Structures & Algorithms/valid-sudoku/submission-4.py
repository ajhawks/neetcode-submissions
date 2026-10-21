class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        verticals = [set() for i in range(9)]
        horizontals = [set() for i in range(9)]
        boxes = [set() for i in range(9)]

        for y in range(9):
            for x in range (9):
                num = board[y][x]
                if num != ".":
                    if int(num) in verticals[y]:
                        return False
                    else:
                        verticals[y].add(int(num))
                    if int(num) in horizontals[x]:
                        return False
                    else:
                        horizontals[x].add(int(num))
                    if int(num) in boxes[x//3 + 3*(y//3) - 1]:
                        return False
                    else:
                        boxes[x//3 + 3*(y//3) - 1].add(int(num))
        return True