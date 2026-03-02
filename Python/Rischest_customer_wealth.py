class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        #method 1:
        #return max(sum(customer) for customer in accounts)

        #method 2:
        max_wealth=0
        for customer in accounts:
            current_wealth=sum(customer)
            max_wealth=max(max_wealth,current_wealth)
        return max_wealth    

        #both methods Time Complexity results: O(N)