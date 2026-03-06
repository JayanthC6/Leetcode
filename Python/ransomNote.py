class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        inventory={}
        for char in magazine:
            inventory[char]=inventory.get(char,0)+1
        for char in ransomNote:
            if inventory.get(char,0)<=0:
                return False
            inventory[char]-=1
        return True            
'''Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

 

Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false
Example 2:

Input: ransomNote = "aa", magazine = "ab"
Output: false
Example 3:

Input: ransomNote = "aa", magazine = "aab"
Output: true'''    