class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Negative numbers are not palindromes
        if x < 0:
            return False
        
        original, rev = x, 0
        while x > 0:
            rev = rev * 10 + x % 10
            x //= 10
        
        return original == rev
