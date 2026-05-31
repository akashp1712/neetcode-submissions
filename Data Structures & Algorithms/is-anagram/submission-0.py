class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        chars = {}

        for char in s:
            chars[char] = chars.get(char, 0) + 1


        for char in t:
            if char in chars:
                chars[char] -= 1

                if chars[char] == 0:
                    del chars[char]
            
            else:
                return False


        return len(chars) == 0
        