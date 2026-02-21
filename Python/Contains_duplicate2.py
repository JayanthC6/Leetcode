'''class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]==nums[j] and abs(i - j) <= k:
                    return True
        return False'''           #Brute force approach
    
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        last = {}
        for i, n in enumerate(nums):
            if n in last and i - last[n] <= k:
                return True
            last[n] = i
        return False

'''Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true
Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false'''