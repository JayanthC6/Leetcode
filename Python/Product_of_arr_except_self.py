class Solution:
    def productExceptSelf(self,nums:list[int])->list[int]:
        n=len(nums)
        ans=[1]*n
        left_product=1
        for i in range(n):
            ans[i]=left_product
            left_product*=nums[i]
        right_product=1
        for i in range(n-1,-1,-1):
            ans[i]*=right_product
            right_product*=nums[i]    
        return ans
#Time Complexity: O(N) where N is the length of the input array nums. We traverse the array twice, once from left to right and once from right to left, resulting in a linear time complexity.
'''Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]'''       