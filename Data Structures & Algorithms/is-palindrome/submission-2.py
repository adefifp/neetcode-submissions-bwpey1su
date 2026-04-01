class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        
        while l < r:
            # Skip non-alphanumeric characters from the left
            if not s[l].isalnum():
                l += 1
            # Skip non-alphanumeric characters from the right
            elif not s[r].isalnum():
                r -= 1
            # Compare characters (case-insensitive)
            else:
                if s[l].lower() != s[r].lower():
                    return False
                l += 1
                r -= 1
                
        return True
            