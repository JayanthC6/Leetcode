class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n=set(nums)
        nums[:]=sorted(n)
        return len(nums)