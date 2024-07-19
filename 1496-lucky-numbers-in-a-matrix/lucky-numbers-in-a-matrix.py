class Solution(object):
    def luckyNumbers(self, matrix):
        min_row = [min(row) for row in matrix]
        max_col = [max(col) for col in zip(*matrix)]      
        lucky_numbers = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == min_row[i] and matrix[i][j] == max_col[j]:
                    lucky_numbers.append(matrix[i][j])
        
        return lucky_numbers