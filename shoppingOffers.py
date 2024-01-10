class Solution:
    def shoppingOffers(self, price, special, needs):
        memo = {}
        return self.shopping(price, special, needs, memo)

    def shopping(self, price, special, needs, memo):
        if tuple(needs) in memo:
            return memo[tuple(needs)]
        cost = sum([price[i] * needs[i] for i in range(len(needs))])
        for offer in special:
            offer_valid = True
            for i in range(len(needs)):
                if offer[i] > needs[i]:
                    offer_valid = False
                    break

            if offer_valid:
                updated_needs = [needs[j] - offer[j] for j in range(len(needs))]
                cost = min(cost, offer[-1] + self.shopping(price, special, updated_needs, memo))

        memo[tuple(needs)] = cost
        return cost
