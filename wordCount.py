#time limit excdeede
class Solution:
    def wordCount(self, startWords: List[str], targetWords: List[str]) -> int:
        def count(i):
            end=[c for c in i]
            for j in startWords:
                start=[c for c in j]
                if len(end)-1==len(start) and all(char in end for char in start):
                    return 1
            return 0
        co=0
        for i in targetWords:
            if count(i):
                co=co+1
        print(co)
        return co
# correct solution
class Solution:
    def wordCount(self, startWords: List[str], targetWords: List[str]) -> int:
        s = set()
        for word in startWords:
            mask = 0
            for c in word:
                mask |= 1 << (ord(c) - ord('a'))
            s.add(mask)

        ans = 0
        for word in targetWords:
            mask = 0
            for c in word:
                mask |= 1 << (ord(c) - ord('a'))
            for c in word:
                t = mask ^ (1 << (ord(c) - ord('a')))
                if t in s:
                    ans += 1
                    break
        return ans
