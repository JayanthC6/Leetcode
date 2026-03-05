class Solution:
    def minOperations(self, s: str) -> int:
        ops=0
        for i in range(len(s)):
            expected_char=str(i%2)
            if s[i]!=expected_char:
                ops+=1
            ops1=len(s)-ops
        return min(ops,ops1)  
#Time Complexity: O(N) where N is the length of the input string s. We iterate through the string once to count the number of operations needed for both patterns.
'''You are given a string s consisting only of the characters '0' and '1'. In one operation, you can change any '0' to '1' or vice versa.

The string is called alternating if no two adjacent characters are equal. For example, the string "010" is alternating, while the string "0100" is not.

Return the minimum number of operations needed to make s alternating.

 

Example 1:

Input: s = "0100"
Output: 1
Explanation: If you change the last character to '1', s will be "0101", which is alternating.
Example 2:

Input: s = "10"
Output: 0
Explanation: s is already alternating.
Example 3:

Input: s = "1111"
Output: 2
Explanation: You need two operations to reach "0101" or "1010".'''             