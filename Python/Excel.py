class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res=""
        while columnNumber>0:
            columnNumber-=1
            char=chr(ord('A') + (columnNumber % 26))
            res=char+res
            columnNumber//=26
        return res    

'''Example 1:

Input: columnNumber = 1
Output: "A"
Example 2:

Input: columnNumber = 28
Output: "AB"
Example 3:

Input: columnNumber = 701
Output: "ZY"'''