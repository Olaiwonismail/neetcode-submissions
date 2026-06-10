class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        hmap = {}
        hs =set()
        vmap = {}
        for l in board:
            for item in l:
                if item in hs and item!='.':
                    return False
                else:
                    hs.add(item)
            hs=set()
        hs=set()
        for n in range(0,9):
            for item in board:
                if item[n] in hs and item[n] !='.':
                    return False
                else:
                    hs.add(item[n])
            hs=set()
        hs=set()
        box={}
        for x in range(0,9):
            for y in range(0,9):
                if not box.get((x//3,y//3)):
                    box[(x//3,y//3)] = set()
                if board[x][y] in box.get((x//3,y//3)) and board[x][y]!='.':
                    return False
                else:
                    box[(x//3,y//3)].add(board[x][y])
                
            

                
        return True