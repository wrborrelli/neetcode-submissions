class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            print(matrix[i][0])
            if matrix[i][0] == target:
                return True
            elif matrix[i][0] > target:
                None
            else:
                try:
                    matrix[i].index(target)
                    return True
                except:
                    None
        return False