# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
'''Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]'''
class Solution:
    def addTwoNumbers(self, l1, l2):
        dummy=ListNode()
        cur=dummy
        carry=0
        while l1 or l2 or carry:
            v1=l1.val if l1 else 0
            v2=l2.val if l2 else 0
            val=v1+v2+carry
            carry=val//10
            val=val%10
            cur.next=ListNode(val)
            cur=cur.next
            l1=l1.next if l1 else None
            l2=l2.next if l2 else None
        return dummy.next    

        
        