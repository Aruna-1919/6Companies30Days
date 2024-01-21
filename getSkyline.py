from queue import PriorityQueue

class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        cuts = set([b[0] for b in buildings] + [b[1] for b in buildings])
        print(cuts)
        pq = PriorityQueue()
        pq.put((0, 2**32))
        i, ans = 0, [(0, 0)]
        for t in sorted(cuts):
            while i < len(buildings) and buildings[i][0] <= t:
                pq.put((-buildings[i][2], buildings[i][1]))
                i += 1
            # pick the highest building at this moment
            # pop the expired item
            while pq.queue[0][1] <= t:
                pq.get()
            high = -pq.queue[0][0]
            if ans[-1][1] != high:
                ans.append((t, high))
        return ans[1:]
