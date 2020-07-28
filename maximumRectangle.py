""""""""""""""""""""""""""""""""
"question: Given a 2D binary matrix filled with 0's and 1's,
" find the largest rectangle containing only 1's and return its area.
"
"


class Solution:
    "Approach 2: Dynamic Programming - Better Brute Force on Histograms"
    def maximalRectangle_2(self, matrix: List[List[str]]) -> int:
       
        if not matrix: return 0
        res = 0
        dp = [[0]*len(matrix[0]) for _ in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]=="0": continue # to next j 
                dp[i][j] = dp[i][j-1]+1 if j else 1
                # compute the maximum area rectangle with a lower right corner at [i, j]
                width = dp[i][j]
                ## exam the column bottom up, right to left
                for k in range(i, -1, -1):
                    width = min(width, dp[k][j])
                    res = max(res, width*(i-k+1))
        return res
                
     # Approach 3:Using histograms-stack and 84. Largest Rectangle in Histogram  
     def maximaRectangle_3(self, matrix: List[List[str]]) -> int:
        
