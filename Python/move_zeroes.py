class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        insert=0
        for num in nums:
            if num!=0:
                nums[insert]=num
                insert+=1
            while insert < len(nums):
                nums[insert] = 0
                insert+=1
        #Time Complexity: O(N)
'''Given an integer array nums, move all 0's to the end of it while maintaining
the relative order of the non-zeroes. Note that you must do this in-place without making a copy of the array.
Example 1:
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]'''     
