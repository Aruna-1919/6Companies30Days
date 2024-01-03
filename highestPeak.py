class Solution(object):
    def highestPeak(self, isWater):
        rows = len(isWater)
        cols = len(isWater[0])
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        
        # Initialize the result grid with -1
        result = [[-1 for _ in range(cols)] for _ in range(rows)]
        queue = []
        
        # Set all water cells to height 0 and add them to the queue
        for i in range(rows):
            for j in range(cols):
                if isWater[i][j] == 1:
                    result[i][j] = 0
                    queue.append((i, j))
        
        while queue:
            current = queue.pop(0)
            x, y = current[0], current[1]
            
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                
                if 0 <= nx < rows and 0 <= ny < cols and result[nx][ny] == -1:
                    result[nx][ny] = result[x][y] + 1
                    queue.append((nx, ny))
        
        return result
