class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        rows=len(mat)
        cols=len(mat[0])
        row_counts=[sum(row) for row in mat]
        col_counts=[sum(col) for col in zip(*mat)]
        spl_positions=0
        for i in range(rows):
            for j in range(cols):
                if mat[i][j]==1 and row_counts[i]==1 and col_counts[j]==1:
                    spl_positions+=1
        return spl_positions            
#Time Complexity: O(M*N) where M is the number of rows and N is the number of columns in the matrix.
'''Given an m x n binary matrix mat, return the number of special positions in mat.

A position (i, j) is called special if mat[i][j] == 1 and all other elements in row i and column j are 0 (rows and columns are 0-indexed).
Input: mat = [[1,0,0],[0,0,1],[1,0,0]]
Output: 1
Explanation: (1, 2) is a special position because mat[1][2] == 1 and all other elements in row 1 and column 2 are 0.

Input: mat = [[1,0,0],[0,1,0],[0,0,1]]
Output: 3
Explanation: (0, 0), (1, 1) and (2, 2) are special positions.'''