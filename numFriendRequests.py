class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        age_count = [0] * 121  # Count the number of people at each age from 0 to 120
        for age in ages:
            age_count[age] += 1

        total_requests = 0
        for ageA in range(15, 121):
            countA = age_count[ageA]
            for ageB in range(int(0.5 * ageA + 7 + 1), ageA + 1):
                countB = age_count[ageB]
                total_requests += countA * countB
                if ageA == ageB:
                    total_requests -= countA  # Remove self-requests

        return total_requests
