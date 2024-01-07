class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        lis = []

        for envelope in envelopes:
            left, right = 0, len(lis)
            height = envelope[1]
            while left < right:
                mid = left + (right - left) // 2
                if lis[mid] < height:
                    left = mid + 1
                else:
                    right = mid

            if right >= len(lis):
                lis.append(height)
            else:
                lis[right] = height

        return len(lis)
