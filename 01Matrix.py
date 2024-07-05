# Time Complexity (BFS Approach) :
# O(M*N)   , M rows and N cols

# Space Complexity (BFS Approach) :  
# O(M*N) , In-place modification

# Approach: 
# Take a queue and start appending the independent items/values in the matrix.
# First, iterate whole matrix and append 0's to queue since we are measuring distance
# of other elements from 0. For 1's, simply mark them as -1
# Now, while queue is not empty, start going through all the 0's is current level,
# and find their 4 neighbors, check if it is -1, then this means that we can update that cell value to 
# "level+1" since we encountered a 1 here. Also, add this element to the queue.
# Keep on processing this above process untill you complete all the elemnets at current level,
# and finally update the level(that is increment by 1)

class Solution(object):
    def updateMatrix(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        # ====== Approach 1: BFS approach ================ #
        if not mat or len(mat)==0:
            return mat
        
        rows = len(mat)
        cols = len(mat[0])

        # Queue
        queue = []

        # dirs
        dirs = [[-1,0],[1,0],[0,-1],[0,1]]

        #level to keep track of level
        level = 0

        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 0:
                    queue.append([i,j])
                else:
                    mat[i][j] = -1

        while queue:
            size = len(queue)
            for j in range(size):
                curr = queue.pop(0)
                for dir in dirs:
                    nr = curr[0] + dir[0]
                    nc = curr[1] + dir[1]
                    if nr>=0 and nr<rows and nc>=0 and nc<cols and mat[nr][nc]== -1:
                        # assign the level+1 to the current cell
                        mat[nr][nc] = level + 1
                        queue.append([nr,nc])
            # increase the level
            level = level+1

        return mat