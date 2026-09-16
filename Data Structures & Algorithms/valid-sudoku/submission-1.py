class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        isRowValid = self.checkRow(board)
        isColValid = self.checkCol(board)
        isGridValid = self.checkGrid(board)

        return isRowValid and isColValid and isGridValid

    def checkGrid(self, board: List[List[str]]) -> bool:
        isValid = True

        for boxRow in range(3):
            if isValid == False:
                break
            for boxCol in range(3):
                if isValid == False:
                    break
                hashSet = set()
                for i in range(3):
                    if isValid == False:
                        break
                    for j in range(3):
                        if board[boxRow * 3 + i][boxCol*3+j] == ".":
                            continue
                        if board[boxRow * 3 + i][boxCol * 3 + j] not in hashSet:
                            hashSet.add(board[boxRow * 3 + i][boxCol*3+j])
                        else:
                            isValid = False
                            break

        return isValid
                
    def checkCol(self, board: List[List[str]]) -> bool:
        isValid = True
        for i in range(len(board)):
            hashSet = set()
            if isValid == False:
                break
            
            for j in range(9):
                if board[j][i] == ".":
                    continue
                if board[j][i] not in hashSet:
                    hashSet.add(board[j][i])
                else:
                    isValid = False
                    break
        return isValid



    def checkRow(self, board: List[List[str]]) -> bool:
        isValid = True
        for i in board:
            hashSet = set()
            print(i)
            if isValid == False:
                break
            
            for j in i:

                if j == ".":
                    continue
                if  j not in hashSet:
                    hashSet.add(j)
                else:
                    isValid = False
                    break
        return isValid