class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        column_number = 0
        for char in columnTitle:
            char_value = ord(char) - ord('A') + 1
            column_number = column_number * 26 + char_value
        return column_number


'''Given a string columnTitle that represents the column title as appears in an Excel sheet, return its corresponding column number.

For example:

A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28 
...
 

Example 1:

Input: columnTitle = "A"
Output: 1
Example 2:

Input: columnTitle = "AB"
Output: 28
Example 3:

Input: columnTitle = "ZY"
Output: 701'''