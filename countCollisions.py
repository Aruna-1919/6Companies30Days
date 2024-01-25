class Solution:
    def countCollisions(self, directions: str) -> int:
        d = directions.lstrip('L').rstrip('R')
        print(d)
        return len(d) - d.count('S')
