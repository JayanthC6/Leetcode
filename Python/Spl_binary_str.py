'''Special binary strings are binary strings with the following two properties:

The number of 0's is equal to the number of 1's.
Every prefix of the binary string has at least as many 1's as 0's.
You are given a special binary string s.

A move consists of choosing two consecutive, non-empty, special substrings of s, and swapping them. 
Two strings are consecutive if the last character of the first string is exactly one index before the 
first character of the second string.
Return the lexicographically largest resulting string possible after applying the mentioned 
operations on the string.
Example 1:
Input: s = "11011000"
Output: "11100100"
Explanation: The strings "10" [occuring at s[1]] and "1100" [at s[3]] are swapped.
This is the lexicographically largest string possible after some number of swaps.'''

class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        count=0
        i=0
        res=[]
        for j,char in enumerate(s):
            if char=='1':
                count+=1
            else:
                count-=1
            if count==0:
                middle_optimize=self.makeLargestSpecial(s[i+1:j])
                res.append('1'+ middle_optimize + '0')
                i=j+1
        res.sort(reverse=True)
        return "".join(res)                
        