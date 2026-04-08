class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # i: the answer is in the i-th row
        # j: the answer is at the j-th column
        start, end = 0, len(matrix) - 1
        while (start <= end):
            i = (start + end) // 2
            if target < matrix[i][0]:
                end = i - 1
            elif target > matrix[i][-1]:
                start = i + 1
            else:
                break

        start, end = 0, len(matrix[i]) - 1
        while (start <= end):
            j = (start + end) // 2
            if target < matrix[i][j]:
                end = j - 1
            elif target > matrix[i][j]:
                start = j + 1
            else:
                return True

        return False