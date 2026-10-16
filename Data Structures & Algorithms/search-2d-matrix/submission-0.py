from math import floor

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        if len(matrix) == 0:
            return False
        
        outerLeft = 0
        outerRight = len(matrix) - 1
        outerMid = floor((outerRight + outerLeft) / 2)

        arr = []
        
        while outerLeft <= outerRight:
            if len(matrix[outerMid]) == 0:
                return False
            elif target >= matrix[outerMid][0] and target <= matrix[outerMid][-1]:
                arr = matrix[outerMid]
                break
            elif target > matrix[outerMid][-1]:
                outerLeft = outerMid + 1
                outerMid = floor((outerRight + outerLeft) / 2)
            else:
                outerRight = outerMid - 1
                outerMid = floor((outerRight + outerLeft) / 2)

        if len(arr) == 0:
            return False

        innerLeft = 0
        innerRight = len(arr) - 1
        innerMid = floor((innerRight + innerLeft) // 2)

        while innerLeft <= innerRight:
            if arr[innerMid] == target:
                return True
            elif target > arr[innerMid]:
                innerLeft = innerMid + 1
                innerMid = floor((innerRight + innerLeft) // 2)
            else:
                innerRight = innerMid - 1
                innerMid = floor((innerRight + innerLeft) // 2)

        return False
