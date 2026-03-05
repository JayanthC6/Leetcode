class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
        max_product=nums[0]
        min_product=nums[0]
        global_max=nums[0]
        for i in range(1,len(nums)):
            num=nums[i]
            temp_max = max(num, max_product * num, min_product * num)
            min_product = min(num, max_product * num, min_product * num)
            max_product = temp_max
            global_max=max(global_max,max_product)
        return global_max    
#Time Complexity: O(N) where N is the length of the input array nums. We traverse the array once, resulting in a linear time complexity.
'''Given an integer array nums, find a subarray that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.

Note that the product of an array with a single element is the value of that element.

 

Example 1:

Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.'''