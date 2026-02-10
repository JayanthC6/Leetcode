class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums=nums1+nums2
        nums.sort()
        n=len(nums)
        l=0
        r=n-1
        m=(l+r)//2
        if n%2==0:
            x=float((nums[m]+nums[m+1])/2)
            return x
        else:
            x=float(nums[m])
            return x    