class Solution:
    def findLongestWord(self, s, dictionary):
        def isSubsequence(word):
            i, j = 0, 0
            while i < len(s) and j < len(word):
                if s[i] == word[j]:
                    j += 1
                i += 1
            return j == len(word)

        longest = ""
        for word in dictionary:
            if isSubsequence(word):
                if len(word) > len(longest) or (len(word) == len(longest) and word < longest):
                    longest = word

        return longest
