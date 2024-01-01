class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        def sum3(s, t, p):
            if t == 0 and len(p) == k:
                result.append(p[:])
                return

            for i in range(s, 10):
                if i > t:
                    break
                if i not in p:
                    p.append(i)
                    sum3(i + 1, t - i, p)
                    p.pop()

        result = []
        sum3(1, n, [])
        return result
