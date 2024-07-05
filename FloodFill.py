# Time Complexity :
# O(M*N)  

# Space Complexity :  
# O(M*N) ,     Recursion stack space

# Approach:
# DFS approach. Start DFS from the given index if the value at that index is not equal to given "color"


class Solution(object):
    def __init__(self):
        self.rows = 0
        self.cols = 0
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        # dfs based approach
        if not image or len(image) == 0:
            return image
        
        self.rows = len(image)
        self.cols = len(image[0])

        if image[sr][sc] == color:
            return image
        
        origColor = image[sr][sc]

        self.dfs(image, sr, sc, color, origColor)

        return image


    def dfs(self, image, row, col, color, origColor):
        #base
        if row<0 or row==self.rows or col<0 or col==self.cols or image[row][col] != origColor:
            return

        # modify color
        image[row][col] = color

        #logic
        self.dfs(image, row-1, col, color, origColor)
        self.dfs(image, row+1, col, color, origColor)
        self.dfs(image, row, col-1, color, origColor)
        self.dfs(image, row, col+1, color, origColor)