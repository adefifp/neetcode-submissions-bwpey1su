class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        check = {}
        for letter in s:
            check[letter] = check.get(letter, 0) + 1
        for letter in t:
            if check.get(letter, 0) == 0:
                return False
            else:
                check[letter] -= 1
        return True