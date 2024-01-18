class Solution(object):
    def allCellsDistOrder(self, rows, cols, rCenter, cCenter):
        result = []
        for r in range(rows):
            for c in range(cols):
                result.append((r, c))
        result = sorted(result, key=lambda point: abs(point[0] - rCenter) + abs(point[1] - cCenter))

        return result
