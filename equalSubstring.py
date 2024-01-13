class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        left = 0
        max_length = 0
        current_cost = 0

        for right in range(len(s)):
            current_cost += abs(ord(s[right]) - ord(t[right]))

            while current_cost > maxCost:
                current_cost -= abs(ord(s[left]) - ord(t[left]))
                left += 1

            max_length = max(max_length, right - left + 1)

        return max_length
