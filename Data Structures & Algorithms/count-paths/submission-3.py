class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        prevRow = [0] * n

        for i in reversed(range(m)):
            currRow = [0] * n
            currRow[n-1] = 1

            for c in reversed(range(n - 1)):
                currRow[c] = currRow[c+1] + prevRow[c]
            prevRow = currRow
        return prevRow[0]